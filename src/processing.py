from typing import List, Dict, Any


def filter_by_state(data_list: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param data_list: Список словарей для фильтрации.
    :param state: Значение состояния, по которому нужно отфильтровать данные. По умолчанию 'EXECUTED'.
    :return: Новый список, содержащий только словари с указанным состоянием.
    """
    return [item for item in data_list if item.get('state') == state]


def sort_by_date(
        data_list: List[Dict[str, Any]],
        descending: bool = True
) -> List[Dict[str, Any]]:
    """
    Возвращает новый список словарей, отсортированный по значению ключа 'date'.

    :param data_list: Список словарей для сортировки.
    :param descending: Если True (по умолчанию), сортировка идет от новых к старым (убывание).
                       Если False — от старых к новым (возрастание).
    :return: Новый отсортированный список словарей.
    """
    # sorted() создает новый список и не изменяет исходный.
    # Обратный порядок задается параметром reverse=descending.
    return sorted(data_list, key=lambda x: x['date'], reverse=descending)