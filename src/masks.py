from typing import Union


def get_mask_card_number(number_card: Union[str]) -> Union[str]:
    """Функция маскировки номера банковской карты"""

    if len(number_card) > 16 or len(number_card) < 16:
        raise ValueError("Такого номера карты не существует")

    return f"{number_card[0:4]} {number_card[4:6]}** **** {number_card[-4:]}"


def get_mask_account(number_account: Union[str]) -> Union[str]:
    """Функция маскировки счета"""
    if number_account == "":
        raise ValueError("Введите номер счета")

    return f"**{number_account[-4:]}"
