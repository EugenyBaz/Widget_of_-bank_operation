from typing import Any


def filter_by_state(list_dict: list[dict[str, Any]], state_str: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция возвращает новый список словарей, у которых ключ state  соответствует определенному значению."""
    new_list = []

    for i in list_dict:
        if i["state"] == state_str:
            new_list.append(i)
    return new_list


def sort_by_date(list_dict: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Функция сортировки по дате по убыванию"""
    sorted_list = sorted(list_dict, key=lambda x: x["date"], reverse=True)

    return sorted_list
