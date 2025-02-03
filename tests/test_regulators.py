import pytest
from src.regulators import search_trans, list_of_trans_user


def  test_search_trans(filter_cur):
    result = search_trans(filter_cur,"Перевод организации")
    assert len(result) == 2
    assert result == [{
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }, {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        }]



def test_list_of_trans_user(filter_cur):
    result = list_of_trans_user(filter_cur, ['Перевод со счета на счет'] )
    assert result == {'перевод со счета на счет':2}