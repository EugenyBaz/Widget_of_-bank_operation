import pytest
from src.widget import mask_account_card, get_date

""" Тест для проверки, что функция корректно распознает и применяет нужный тип маскировки"""


@pytest.fixture
def number_card():
    return ['Mastercard 1111222233334444', 'Счет 89706059432112345678']


@pytest.mark.parametrize("number_card, expected", [('Mastercard 1111222233334444', 'Mastercard 1111 22** **** 4444'),
                                                   ('Счет 89706059432112345678', 'Счет **5678')])
def test_mask_account_card(number_card, expected):
    assert mask_account_card(number_card) == expected
#
# def test_get_mask_invalid_card_number(number_card):
#     with pytest.raises(ValueError):
#         get_mask_card_number('111')
#
#
# @pytest.fixture
# def number_account():
#     return ['12345678900987654321', '89706059432112345678']
#
#
# @pytest.mark.parametrize("number_account, expected", [('12345678900987654321', '**4321'),
#                                                       ('89706059432112345678', '**5678')])
# def test_get_mask_account(number_account, expected):
#     assert get_mask_account(number_account) == expected
#
# def test_get_mask_invalid_account(number_account):
#     with pytest.raises(ValueError):
#         get_mask_account('')
