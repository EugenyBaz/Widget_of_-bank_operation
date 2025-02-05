import json
import logging
import os
from typing import Any, Dict, List

from src.external_second_api import convert_currency

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
data_file_path = os.path.join(project_root, "logs", "utils.log")


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(data_file_path)
file_formatter = logging.Formatter(
    "%(levelname)s: %(name)s: Request time: %(asctime)s: %(message)s", "%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_file_trans(list_tr: str) -> List[Dict[str, Any]]:
    """Функция конвертации файла json в список python"""
    logger.info("Запуск функции конвертации файла json в список python")
    operations_list: List[Dict[str, Any]] = []

    try:

        with open(list_tr, "r", encoding="utf-8") as file:
            operations_list = json.load(file)

        if not isinstance(operations_list, list):
            logger.warning("Ошибка- файл содержит не список")
            raise TypeError("Файл содержит не список")

    except FileNotFoundError:
        logger.warning("Ошибка- файл не найден FileNotFoundError ")
        print([])
    except TypeError:
        logger.warning("Ошибка- TypeError ")
        print([])
    except json.JSONDecodeError:
        logger.warning("Ошибка- JSONDecodeError")
        print([])

    return operations_list


def convert_transaction(list_trans: List[Dict[str, Any]]) -> Any:
    """Функция вывода суммы транзакций"""
    logger.info("Запуск функции подсчета суммы транзакции")
    list_RUB = []
    list_USD = []
    list_EUR = []

    for transaction in list_trans:
        if "operationAmount" in transaction:
            currency_code = transaction["operationAmount"]["currency"]["code"]
            amount = float(transaction["operationAmount"]["amount"])

            if currency_code == "USD":
                list_USD.append(amount)
            elif currency_code == "RUB":
                list_RUB.append(amount)
            elif currency_code == "EUR":
                list_EUR.append(amount)

    sum_rub = sum(list_RUB)
    sum_usd = sum(list_USD) * convert_currency("USD")
    sum_eur = sum(list_EUR) * convert_currency("EUR")
    total_usd = round(sum_rub + sum_usd + sum_eur, 2)

    return total_usd


if __name__ == "__main__":
    list_trans = read_file_trans("../data/operations.json")
    conv_trans = convert_transaction(list_trans)

    print(list_trans)
    logger.info("Вывод на печать в консоль результата функции конвертации ")

    print(conv_trans)
    logger.info("Вывод подсчета суммы транзакции в консоль")
