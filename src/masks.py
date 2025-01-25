from typing import Union
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log")
file_formatter = logging.Formatter(
    "%(levelname)s: %(name)s: Request time: %(asctime)s: %(message)s", "%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(number_card: Union[str]) -> Union[str]:
    """Функция маскировки номера банковской карты"""
    logger.info(f"Запуск функции маскировки номера банковской карты")
    if len(number_card) > 16 or len(number_card) < 16:
        logger.warning(f"Ошибка -такого номера карты не существует")
        raise ValueError("Такого номера карты не существует")

    return f"{number_card[0:4]} {number_card[4:6]}** **** {number_card[-4:]}"


def get_mask_account(number_account: Union[str]) -> Union[str]:
    """Функция маскировки счета"""
    logger.info(f"Запуск функции маскировки счета")
    if number_account == "":
        logger.warning(f"Ошибка - такого номера счета не существует")
        raise ValueError("Введите номер счета")

    return f"**{number_account[-4:]}"
