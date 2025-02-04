import json
import os
from typing import Any
import csv
import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
data_file_path = os.path.join(project_root, "data", "transactions.csv")
data_file_path_exl = os.path.join(project_root, "data", "transactions_excel.xlsx")


def read_transactions_csv(file_path: Any = data_file_path) -> str:
    """ Функция получения, чтения файла cvs, преобразование в список словарей транзакций"""

    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file,delimiter=";")
        transactions = list(reader)
        return transactions


if __name__ == "__main__":

    transactions_csv = read_transactions_csv()
    print(transactions_csv)


def read_transactions_exl(file_path: Any) -> str:
    """Функция получения, чтения файла excel, преобразование в список словарей транзакций"""
    df = pd.read_excel(file_path)
    list_transactions_exl = df.to_dict(orient="records")
    return list_transactions_exl


if __name__ == "__main__":

    transactions_list = read_transactions_exl(data_file_path_exl)
    print(transactions_list)
