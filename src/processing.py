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


print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)

def sort_by_date(list_dict: [str | int]) -> [str | int]:
    """ Функция сортировки по дате по убыванию"""
    sorted_list = sorted(list_dict, key=lambda x: x['date'], reverse=True)

    return sorted_list