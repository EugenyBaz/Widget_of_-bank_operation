from typing import Union


def get_mask_card_number(number_card: Union[str]) -> Union[str]:
    """Функция маскировки номера банковской карты"""

    return f"{number_card[0:4]} {number_card[4:6]}** **** {number_card[-4:]}"


def get_mask_account(number_account: Union[str]) -> Union[str]:
    """Функция маскировки счета"""

    return f"**{number_account[-4:]}"
