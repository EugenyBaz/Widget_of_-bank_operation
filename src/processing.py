from typing import Union


def filter_by_state(list_dict: [str | int]) -> [str | int]:
    """Функция возвращает новый список словарей, у которых ключ state  соответствует определенному значению."""
    list_ex = []
    list_cncl = []
    for i in list_dict:
        if i["state"] == "EXECUTED":
            list_ex.append(i)
        elif i["state"] == "CANCELED":
            list_cncl.append(i)
    return f"{list_ex}\n{list_cncl}"




def sort_by_date(list_dict: [str | int]) -> [str | int]:
    """ Функция сортировки по дате по убыванию"""
    sorted_list = sorted(list_dict, key=lambda x: x['date'], reverse=True)

    return sorted_list