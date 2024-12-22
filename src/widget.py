from typing import Union


def mask_account_card(number_card: Union[str]) -> Union[str]:
    """Функция маскировки номера банковской карты или счета"""

    if number_card[:4] == "Счет" and len(number_card) != 25:
        raise ValueError("Введен не корректный счет")

    if number_card[:4] == "Счет":
        return f"{number_card[0 - len(number_card):-20]}**{number_card[-4:]}"
    else:
        return (
            f"{number_card[0 - len(number_card):-16]}{number_card[-16:-12]}"
            f" {number_card[-10:-8]}** **** {number_card[-4:]}"
        )


def get_date(date: Union[str]) -> Union[str]:
    """Форматирование даты"""
    if date == "":
        raise ValueError("Введите дату")
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
