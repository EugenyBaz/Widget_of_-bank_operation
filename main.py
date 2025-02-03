from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from src.decorators import my_function
from src.reader_csv_excel import  read_transactions_csv, read_transactions_exl
from src.regulators import search_trans
import os
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ""))
data_file_path = os.path.join(project_root, "data", "transactions.csv")
data_file_path_exl = os.path.join(project_root, "data", "transactions_excel.xlsx")
data_file_path_json = os.path.join(project_root, "data", "operations.json")

print("""Привет! Добро пожаловать в программу работы с банковскими транзакциями.""")
""" 1.Приветствие """

user_input = input(
"""Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
""")
""" 2. Выбор файлов """

if user_input == "1":
    print ("""Для обработки выбран JSON-файл """)

if user_input == "2":
    print ("""Для обработки выбран CSV-файл """)

if user_input == "3":
    print("""Для обработки выбран XLSX-файл """)


state = input("""Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
""" 3. Выбор статусов """

state_str= state.upper()

if user_input == "1":
    with open(data_file_path_json, 'r', encoding= "utf-8") as file:
        trans_list_conv = json.load(file)
    result_user = filter_by_state(trans_list_conv, state_str)
    print(result_user)

elif user_input == "2":
    file_json = read_transactions_csv(data_file_path)
    result_user= filter_by_state(file_json, state_str)
    print(result_user)

elif user_input == "3":
    file_json = read_transactions_exl(data_file_path_exl)
    result_user = filter_by_state(file_json, state_str)
    print(result_user)

user_input_sort = input("""Отсортировать операции по дате? Да/Нет
""").lower()
""" 4. Сортировка по дате  """

if user_input_sort == "да":

    reverse = input("""Отсортировать по убыванию или возрастанию?
""").lower()

    if reverse == "убыванию":
        reverse_str = True
    elif reverse == "возрастанию":
        reverse_str = False
    else:
        print("Некорректный выбор пользователя.")

    result_sort = sort_by_date(result_user, reverse_str)
    print(result_sort)

elif user_input_sort == "нет":

    print(result_user)

user_input_currency = input("""Выводить только рублевые транзакции? Да/Нет
""").lower()
""" 5. Фильтр по валюте  """

if user_input_currency == "да":
    currency = "RUB"
    if user_input_sort == "да":
        user_cur = list(filter_by_currency(result_sort, currency))
        print(user_cur)
    else:
        print("Некорректный выбор пользователя.")

else:
    user_cur = result_user
    print(user_cur)


user_input_trans = input("""Отфильтровать список транзакций по определенному слову 
в описании? Да/Нет""").lower()
""" 6. Фильтр по слову в названии транзакции  """

if user_input_trans == "да":
    search = input("Введите название транзакции ")
    if user_input_trans == "да":
        user_trans = search_trans(user_cur, search)
    else:
        user_trans= list(filter_by_currency(result_user, currency))
    print(user_trans)

elif user_input_trans == "нет":
    user_trans = user_cur
    print(user_trans)

print (""" ↓↓↓ РАСПЕЧАТЫВАЮ ИТОГОВЫЙ СПИСОК ТРАНЗАКЦИЙ ↓↓↓ """)
""" 7. Итоговый вывод отчета  """


for t in user_trans:
    if t['description'] == 'Открытие вклада':
        print(f"{get_date(t['date'])} {t['description']}\n{mask_account_card(t['to'])}\nСумма:{t['operationAmount']['amount']} {t['operationAmount']['currency']['name']}\n")
    elif t['description'] == 'Перевод с карты на карту':
        print(f"{get_date(t['date'])} {t['description']}\n{mask_account_card(t['from'])} -> {mask_account_card(t['to'])}\nСумма:{t['operationAmount']['amount']} {t['operationAmount']['currency']['name']}\n")
    elif t['description'] == 'Перевод организации':
        print(f"{get_date(t['date'])} {t['description']}\n{mask_account_card(t['from'])} -> {mask_account_card(t['to'])}\nСумма:{t['operationAmount']['amount']} {t['operationAmount']['currency']['name']}\n")
    elif t['description'] == 'Перевод со счета на счет':
        print(f"{get_date(t['date'])} {t['description']}\n{mask_account_card(t['from'])} -> {mask_account_card(t['to'])}\nСумма:{t['operationAmount']['amount']} {t['operationAmount']['currency']['name']}\n")








# if __name__ == "__main__":
#     number_card = input("Введите номер карты")
#     """Вывод номера карты в скрытом виде"""
#
# print(get_mask_card_number(number_card))
#
# number_account = input("Введите номер счета")
# """Вывод номера счета в скрытом виде"""
#
# print(get_mask_account(number_account))
#
# if __name__ == "__main__":
#     """ Приведение в нужный формат даты"""
#     number_card = input("Введите номер карты или счета")
#     print(mask_account_card(number_card))
#
#     date = input("Введите дату")
#     print(get_date(date))
#
# # if __name__ == "__main__":
#     """ Фильтрация по введенному  статусу "CANCELED" или "EXECUTED" """
#     state = input("Введите статус")
#     state_str = state.upper()
#
#     print(
#         filter_by_state(
#             [
#                 {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#                 {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#                 {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#                 {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#             ],
#             state_str,
#         )
#     )
#
# # if __name__ == "__main__":

    # """ Сортировка по True и False"""
    #
    # reverse = input("Введите порядок сортировки True(сначала новые) или False(сначала ранние)")
    # reverse_up = reverse.title()
    # if reverse_up == "True":
    #     reverse_str = True
    # else:
    #     reverse_str = False
    #
    # print(
    #     sort_by_date(
    #         [
    #             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    #             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    #             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    #             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    #         ],
    #         reverse_str,
    #     )
    # )

    #
    # """ Сортировка по валюте USD или RUB"""
    #
    # transactions = (
    #     [
    #         {
    #             "id": 939719570,
    #             "state": "EXECUTED",
    #             "date": "2018-06-30T02:08:58.425572",
    #             "operationAmount": {
    #                 "amount": "9824.07",
    #                 "currency": {
    #                     "name": "USD",
    #                     "code": "USD"
    #                 }
    #             },
    #             "description": "Перевод организации",
    #             "from": "Счет 75106830613657916952",
    #             "to": "Счет 11776614605963066702"
    #         },
    #         {
    #             "id": 142264268,
    #             "state": "EXECUTED",
    #             "date": "2019-04-04T23:20:05.206878",
    #             "operationAmount": {
    #                 "amount": "79114.93",
    #                 "currency": {
    #                     "name": "USD",
    #                     "code": "USD"
    #                 }
    #             },
    #             "description": "Перевод со счета на счет",
    #             "from": "Счет 19708645243227258542",
    #             "to": "Счет 75651667383060284188"
    #         },
    #         {
    #             "id": 873106923,
    #             "state": "EXECUTED",
    #             "date": "2019-03-23T01:09:46.296404",
    #             "operationAmount": {
    #                 "amount": "43318.34",
    #                 "currency": {
    #                     "name": "руб.",
    #                     "code": "RUB"
    #                 }
    #             },
    #             "description": "Перевод со счета на счет",
    #             "from": "Счет 44812258784861134719",
    #             "to": "Счет 74489636417521191160"
    #         },
    #         {
    #             "id": 895315941,
    #             "state": "EXECUTED",
    #             "date": "2018-08-19T04:27:37.904916",
    #             "operationAmount": {
    #                 "amount": "56883.54",
    #                 "currency": {
    #                     "name": "USD",
    #                     "code": "USD"
    #                 }
    #             },
    #             "description": "Перевод с карты на карту",
    #             "from": "Visa Classic 6831982476737658",
    #             "to": "Visa Platinum 8990922113665229"
    #         },
    #         {
    #             "id": 594226727,
    #             "state": "CANCELED",
    #             "date": "2018-09-12T21:27:25.241689",
    #             "operationAmount": {
    #                 "amount": "67314.70",
    #                 "currency": {
    #                     "name": "руб.",
    #                     "code": "RUB"
    #                 }
    #             },
    #             "description": "Перевод организации",
    #             "from": "Visa Platinum 1246377376343588",
    #             "to": "Счет 14211924144426031657"
    #         }
    #     ]
    # )
    #
    # cur = input("Введите валюту USD или RUB")
    # currency = cur.upper()
    #
    # usd_transactions = list(filter_by_currency(transactions, currency))
    #
    # for transaction in usd_transactions:
    #     print(transaction)

# if __name__ == "__main__":
#     """ Вывод описаний транзакций по ключу "discriptions"""
#
#     transactions = (
#         [
#             {
#                 "id": 939719570,
#                 "state": "EXECUTED",
#                 "date": "2018-06-30T02:08:58.425572",
#                 "operationAmount": {
#                     "amount": "9824.07",
#                     "currency": {
#                         "name": "USD",
#                         "code": "USD"
#                     }
#                 },
#                 "description": "Перевод организации",
#                 "from": "Счет 75106830613657916952",
#                 "to": "Счет 11776614605963066702"
#             },
#             {
#                 "id": 142264268,
#                 "state": "EXECUTED",
#                 "date": "2019-04-04T23:20:05.206878",
#                 "operationAmount": {
#                     "amount": "79114.93",
#                     "currency": {
#                         "name": "USD",
#                         "code": "USD"
#                     }
#                 },
#                 "description": "Перевод со счета на счет",
#                 "from": "Счет 19708645243227258542",
#                 "to": "Счет 75651667383060284188"
#             },
#             {
#                 "id": 873106923,
#                 "state": "EXECUTED",
#                 "date": "2019-03-23T01:09:46.296404",
#                 "operationAmount": {
#                     "amount": "43318.34",
#                     "currency": {
#                         "name": "руб.",
#                         "code": "RUB"
#                     }
#                 },
#                 "description": "Перевод со счета на счет",
#                 "from": "Счет 44812258784861134719",
#                 "to": "Счет 74489636417521191160"
#             },
#             {
#                 "id": 895315941,
#                 "state": "EXECUTED",
#                 "date": "2018-08-19T04:27:37.904916",
#                 "operationAmount": {
#                     "amount": "56883.54",
#                     "currency": {
#                         "name": "USD",
#                         "code": "USD"
#                     }
#                 },
#                 "description": "Перевод с карты на карту",
#                 "from": "Visa Classic 6831982476737658",
#                 "to": "Visa Platinum 8990922113665229"
#             },
#             {
#                 "id": 594226727,
#                 "state": "CANCELED",
#                 "date": "2018-09-12T21:27:25.241689",
#                 "operationAmount": {
#                     "amount": "67314.70",
#                     "currency": {
#                         "name": "руб.",
#                         "code": "RUB"
#                     }
#                 },
#                 "description": "Перевод организации",
#                 "from": "Visa Platinum 1246377376343588",
#                 "to": "Счет 14211924144426031657"
#             }
#         ]
#     )
#
#     descriptions = transaction_descriptions(transactions)
#
#     for i in range(5):
#         print(next(descriptions))
#
# if __name__ == "__main__":
#     """ Генерация номера карты по заданному диапазону"""
#
#     while True:
#         start_1 = input("Введите начало диапазона")
#         stop_1 = input("Введите конец диапазона")
#
#         try:
#             start = int(start_1)
#             stop = int(stop_1)
#
#             break
#
#         except ValueError:
#             print("Введённые значения должны быть целыми числами. Попробуйте снова.")
#
#     for card_number in card_number_generator(start, stop):
#         print(card_number)

if __name__ == "__main__":
    """Функция с декораторами записи логов со временем начала и конца, так же
    с выводом ошибок в консоль, либо в mylog.txt"""
    my_function(1, 2)







