import pytest
from src.masks import get_mask_card_number, get_mask_account
from typing import List


@pytest.fixture
def number_card(number: str) -> List[str]:

    return ["1111222233334444", "6666222233339999"]


@pytest.mark.parametrize(
    "number_card, expected", [("1111222233334444", "1111 22** **** 4444"), ("6666222233339999", "6666 22** **** 9999")]
)
def test_get_mask_card_number(number_card: str, expected: str) -> None:
    """Тестирование на правильность маскировки карты"""
    assert get_mask_card_number(number_card) == expected


def test_get_mask_invalid_card_number(number_card: str) -> None:
    """Тестирование на вызов ошибки при некорректном вводе номера карты"""
    with pytest.raises(ValueError):

        get_mask_card_number("111")


@pytest.fixture
def number_account(numbet: str) -> List[str]:
    return ["12345678900987654321", "89706059432112345678"]


@pytest.mark.parametrize(
    "number_account, expected", [("12345678900987654321", "**4321"), ("89706059432112345678", "**5678")]
)
def test_get_mask_account(number_account: str, expected: str) -> None:
    """Тестирование на правильность маскировки счета"""
    assert get_mask_account(number_account) == expected


def test_get_mask_invalid_account(number_account: str) -> None:
    """Тестирование на вызов ошибки при вводе пустого списка"""
    with pytest.raises(ValueError):
        get_mask_account("")
