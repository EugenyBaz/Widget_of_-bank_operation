from typing import Dict, List, Union


def filter_by_state(list_dict: List[Dict[str,Union[str, int]]],
                    state_str: str = "EXECUTED") -> List[Dict[str,Union[str, int]]]:
    """Функция возвращает новый список словарей, у которых ключ state  соответствует определенному значению."""
    new_list = []

    for i in list_dict:
        if  i["state"] == state_str:
            new_list.append(i)
    return new_list



def sort_by_date(list_dict: List[Dict[str,Union[str, int]]],
                 reverse_str: bool = True) -> List[Dict[str,Union[str, int]]]:
    """Функция сортировки по дате по убыванию"""
    for i in list_dict:
        if i["date"] == "":
            raise ValueError( "Отсутствует дата")


    sorted_list = sorted(list_dict, key=lambda x: x["date"], reverse=reverse_str)

    return sorted_list
