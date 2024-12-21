import pytest
from src.masks import get_mask_card_number, get_mask_account

""" Тестирование на правильность маскировки карты"""


@pytest.fixture
def number_card():
    return ['1111222233334444', '6666222233339999']


@pytest.mark.parametrize("number_card, expected", [('1111222233334444', '1111 22** **** 4444'),
                                                   ('6666222233339999', '6666 22** **** 9999')])
def test_get_mask_card_number(number_card, expected):
    assert get_mask_card_number(number_card) == expected

def test_get_mask_invalid_card_number(number_card):
    with pytest.raises(ValueError):
        get_mask_card_number('111')


@pytest.fixture
def number_account():
    return ['12345678900987654321', '89706059432112345678']


@pytest.mark.parametrize("number_account, expected", [('12345678900987654321', '**4321'),
                                                      ('89706059432112345678', '**5678')])
def test_get_mask_account(number_account, expected):
    assert get_mask_account(number_account) == expected

def test_get_mask_invalid_account(number_account):
    with pytest.raises(ValueError):
        get_mask_account('')

