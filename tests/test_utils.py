import pytest
from unittest.mock import patch, mock_open
import json
from src.utils import read_file_trans, convert_transaction
from typing import Dict, List, Any


def test_read_file_success(list_tr: List[Dict[str,Any]])-> None:
    with patch(
        "builtins.open", mock_open(read_data=json.dumps([{"operation": "deposit", "amount": 100}]))
    ) as mock_file:
        result = read_file_trans(list_tr)
        mock_file.assert_called_once_with(list_tr, "r", encoding="utf-8")
        assert result == [{"operation": "deposit", "amount": 100}]


def test_file_not_found_error(list_tr: List[Dict[str,Any]])-> None:
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = read_file_trans(list_tr)
        assert result == []


def test_type_error(list_tr: List[Dict[str,Any]])-> None:
    with patch("builtins.open", mock_open(read_data="not a valid json")):
        result = read_file_trans(list_tr)
        assert result == []


@pytest.mark.parametrize(
    "short_list, expected",
    [
        (
            [
                {
                    "id": 441945886,
                    "state": "EXECUTED",
                    "date": "2019-08-26T10:50:58.294041",
                    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Maestro 1596837868705199",
                    "to": "Счет 64686473678894779589",
                },
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                    "operationAmount": {"amount": "8221.37", "currency": {"name": "RUB", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "MasterCard 7158300734726758",
                    "to": "Счет 35383033474447895560",
                },
            ],
            40178.95,
        )
    ],
)
def test_convert_transaction(short_list: List[Dict[str,Any]], expected: str)-> None:
    assert convert_transaction(short_list) == expected
