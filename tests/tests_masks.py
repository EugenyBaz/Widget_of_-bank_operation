import pytest
from src.masks import get_mask_card_number


@pytest.fixture
def number():
    return ['1111222233334444', '5555666677778888', '99990000011112222']


@pytest.mark.parametrize("expected", (['1111 22** ***** 4444',
                                       '5555 66** ***** 8888',
                                       '9999 00** ***** 2222']))
def test_get_mask_card_number(number, expected):
    assert get_mask_card_number(number) == expected
