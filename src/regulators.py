from src.utils import read_file_trans
import re
from collections import Counter

def search_trans(transactions, search):
    """ Функция выборки транзакций по названию """
    results = []
    pattern = re.compile(search, flags=re.IGNORECASE)
    for trans in transactions:
        if "description" in trans and pattern.search(trans["description"]):
            results.append(trans)
    return results


def list_of_trans_user(transactions, categories):
    """ Подсчет количества транзакций по заданным категориям"""
    result = []

    for trans in transactions:
        if "description" in trans:
            desc = trans['description'].lower()
            for category in categories:
                if category.lower() in desc:
                    result.append(desc)

    counted = Counter(result)

    return dict(counted)

transactions =  read_file_trans("../data/operations.json")

if __name__ == "__main__":
    user_input = input("Введите список категорий, разделенных запятыми: ")
    categories = [category.strip().lower() for category in user_input.split(",")]
    print (list_of_trans_user(transactions, categories))
