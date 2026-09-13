import re


def mask_card_number(card_number):
    """Возвращает замаскированный номер карты."""
    # Оставляем первые 6 цифр, заменяем следующие 6 звездочками,
    # оставляем пробел перед последними 4 цифрами.
    return f"{card_number[:6]} {card_number[6:8]}** **** {card_number[-4:]}"


def mask_account_number(account_number):
    """Возвращает замаскированный номер счёта."""
    # Оставляет только последние 4 цифры.
    return account_number[-4:]


def mask_account_card(full_string: str) -> str:
    """
    Маскирует информацию о карте или счете, полученную одной строкой.

    Args:
        full_string (str): Строка вида "Тип 1234567890123456"
            (где Тип может быть Visa, Maestro, Счет и т.д.).

    Returns:
        str: Исходная строка с замаскированным номером.
    """

    # Находим название типа (текст до первого числа)
    name_part = re.match(r'^\D+', full_string).group(0).strip()

    # Находим сам номер (последовательность из 16+ цифр).
    number_match = re.search(r'\d{16,}', full_string)

    if not number_match:
        raise ValueError("Номер карты/счета не найден")

    number_part = number_match.group(0)

    # Определяем тип по названию
    if 'счет' in name_part.lower():
        masked_number = mask_account_number(number_part)
    else:
        masked_number = mask_card_number(number_part)

    # Собираем результат обратно в строку
    result = f"{name_part} {masked_number}"

    return result.strip()


from datetime import datetime


def get_date(iso_string):
    """
    Преобразует дату из строки в формате ISO (например, "2024-03-11T02:26:18.671407")
    в строку вида ДД.ММ.ГГГГ ("11.03.2024").

    Args:
        iso_string (str): Строка с датой в формате ISO.

    Returns:
        str: Дата в формате ДД.ММ.ГГГГ.
    """

    # Парсим строку по формату ISO 8601.
    # Метод fromisoformat() отлично справляется со строками типа YYYY-MM-DDTHH:MM:SS.mmmmmm,
    # но он не понимает миллисекунды после точки (только до запятой).
    # Поэтому мы просто обрезаем всё лишнее после символа 'T'.
    date_obj = datetime.fromisoformat(iso_string.split('T')[0])

    # Возвращаем результат в нужном виде через метод format().
    return date_obj.strftime('%d.%m.%Y')