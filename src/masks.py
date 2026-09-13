def get_mask_card_number(card_number):
    """Функция принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и отображается в формате
    XXXX XX** **** XXXX"""

    clean_num = ""
    # Шаг 1: Только очистка данных
    for char in str(card_number):
        if char.isdigit():
            clean_num += char

    # Шаг 2: Проверка валидности ПОСЛЕ сбора всех цифр
    if len(clean_num) < 10:
        raise ValueError("Номер карты слишком короткий для применения маски.")

    # Шаг 3: Формирование маски ВНЕ цикла
    first_six = clean_num[:6]
    last_four = clean_num[-4:]

    block_1 = first_six[:4]  # Первые 4 цифры
    block_2 = first_six[4:] + "**"  # 5-6 цифры + звездочки
    block_3 = "****"  # Центральный блок
    block_4 = last_four  # Последние 4 цифры

    return f"{block_1} {block_2} {block_3} {block_4}"


def get_mask_account(account_number):
    """Функция принимает на вход номер счета и возвращает его маску"""

    # Шаг 1: Очистка данных (только цифры) — РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
    clean_num = ""
    for char in str(account_number):
        if char.isdigit():
            clean_num += char

    # Шаг 2: Проверка валидности ПОСЛЕ сбора всех цифр
    if len(clean_num) < 4:
        raise ValueError("Номер счета должен содержать минимум 4 цифры.")

    # Шаг 3: Формирование маски ВНЕ цикла
    last_four = clean_num[-4:]

    return f"**{last_four}"
