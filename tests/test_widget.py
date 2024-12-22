import pytest
from src.widget import mask_account_card, get_date
from typing import List


@pytest.fixture
def number_card(number: str) -> List[str]:
    return ["Mastercard 1111222233334444", "Счет 89706059432112345678"]


@pytest.mark.parametrize(
    "number_card, expected",
    [("Mastercard 1111222233334444", "Mastercard 1111 22** **** 4444"), ("Счет 89706059432112345678", "Счет **5678")],
)
def test_mask_account_card(number_card: str, expected: str) -> None:
    """Тест для проверки, что функция корректно распознает и применяет нужный тип маскировки"""
    assert mask_account_card(number_card) == expected


def test_mask_invalid_account_card(number_card: str) -> None:
    """Тест для проверки вызова ошибки при некорректном введении номера счета"""
    with pytest.raises(ValueError):
        mask_account_card("Счет 8970605943211234567")


@pytest.fixture
def date(date: str) -> List[str]:
    return ["2024-03-11T02:26:18.671407", "2024-12-31"]


@pytest.mark.parametrize(
    "date, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2024-12-31", "31.12.2024")]
)
def test_get_date(date: str, expected: str) -> None:
    """Тест для проверки функции корректной конвертации формата даты"""
    assert get_date(date) == expected


def test_get_invalid_date(date: str) -> None:
    """Тест для проверки вызова ошибки при отсутствии даты"""
    with pytest.raises(ValueError):
        get_date("")
