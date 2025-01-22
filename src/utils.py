import json
from src.external_second_api import convert_currency

def read_file_trans(list_tr):
    operations_list = []

    try :

        with open(list_tr, 'r' , encoding='utf-8') as file:
            operations_list = json.load(file)

        if not isinstance(operations_list, list):
            raise TypeError("Файл содержит не список")

    except FileNotFoundError:
        print([])
    except TypeError:
        print([])
    except json.JSONDecodeError:
        print([])

    return operations_list

list_trans = read_file_trans('../data/operations.json')

print (list_trans)

def convert_transaction(list_trans):
    list_RUB = []
    list_USD = []
    list_EUR = []

    for transaction in list_trans:
        if 'operationAmount' in transaction:
            currency_code = transaction['operationAmount']['currency']['code']
            amount = float(transaction['operationAmount']['amount'])

            if currency_code == "USD":
                list_USD.append(amount)
            elif currency_code == "RUB":
                list_RUB.append(amount)
            elif currency_code == "EUR":
                list_EUR.append(amount)

    sum_rub = sum(list_RUB)
    sum_usd = sum(list_USD) * convert_currency("USD")
    sum_eur = sum(list_EUR) * convert_currency("EUR")
    total_usd = round((sum_rub + sum_usd + sum_eur),2)

    return total_usd

conv_trans = convert_transaction(list_trans)

print(conv_trans)







