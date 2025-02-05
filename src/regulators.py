from src.utils import read_file_trans
import re
from collections import Counter
from typing import List, Dict, Any


def search_trans(transactions: List[Dict[str, Any]], search: str) -> List[Dict[str, Any]]:
    """Функция выборки транзакций по названию"""
    results = []
    pattern = re.compile(search, flags=re.IGNORECASE)
    for trans in transactions:
        if "description" in trans and pattern.search(trans["description"]):
            results.append(trans)
    return results


def list_of_trans_user(transactions: List[Dict[str, Any]], categories: Any) -> dict:
    """Подсчет количества транзакций по заданным категориям"""
    result = []

    for trans in transactions:
        if "description" in trans:
            desc = trans["description"].lower()
            for category in categories:
                if category.lower() in desc:
                    result.append(desc)

    counted = Counter(result)

    return dict(counted)


transactions = read_file_trans("../data/operations.json")

if __name__ == "__main__":
    user_input = input("Введите список категорий, разделенных запятыми: ")
    categories = [category.strip().lower() for category in user_input.split(",")]
    print(list_of_trans_user(transactions, categories))
    print(type(list_of_trans_user(transactions, categories)))
