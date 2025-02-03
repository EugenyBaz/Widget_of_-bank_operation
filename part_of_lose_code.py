from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date



trans = [{'id': 801684332, 'state': 'EXECUTED', 'date': '2019-11-05T12:04:13.781725', 'operationAmount': {'amount': '21344.35', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Открытие вклада', 'to': 'Счет 77613226829885488381'}, {'id': 108066781, 'state': 'EXECUTED', 'date': '2019-06-21T12:34:06.351022', 'operationAmount': {'amount': '25762.92', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Открытие вклада', 'to': 'Счет 90817634362091276762'}, {'id': 285353808, 'state': 'EXECUTED', 'date': '2018-08-06T16:22:54.643491', 'operationAmount': {'amount': '82946.19', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Открытие вклада', 'to': 'Счет 12189246980267075758'}, {'id': 596171168, 'state': 'EXECUTED', 'date': '2018-07-11T02:26:18.671407', 'operationAmount': {'amount': '79931.03', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Открытие вклада', 'to': 'Счет 72082042523231456215'}, {'id': 587085106, 'state': 'EXECUTED', 'date': '2018-03-23T10:45:06.972075', 'operationAmount': {'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Открытие вклада', 'to': 'Счет 41421565395219882431'}, {'id': 893507143, 'state': 'EXECUTED', 'date': '2018-02-03T07:16:28.366141', 'operationAmount': {'amount': '90297.21', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Открытие вклада', 'to': 'Счет 37653295304860108767'}]

for t in trans:
    print(f"{get_date(t['date'])} {t['description']}\n{mask_account_card(t['to'])}\nСумма:{t['operationAmount']['amount']} {t['operationAmount']['currency']['name']}")




#
# current_dir = os.path.dirname(os.path.abspath(__file__))
# project_root = os.path.abspath(os.path.join(current_dir, ""))
# data_file_path = os.path.join(project_root, "data", "transactions.csv")
# data_file_path_exl = os.path.join(project_root, "data", "transactions_excel.xlsx")
# data_file_path_json = os.path.join(project_root, "data", "operations.json")
#
# result_user_one = None
# result_user_two = None
# result_user_three = None
#
# if user_input == "1":
#     with open(data_file_path_json, 'r', encoding= "utf-8") as file:
#         trans_list_conv = json.load(file)
#     result_user_one = filter_by_state(trans_list_conv, state_str)
#     print(result_user_one)
#
# elif user_input == "2":
#     file_json = read_transactions_csv(data_file_path)
#     result_user_two = filter_by_state(file_json, state_str)
#     print(result_user_two)
#
# elif user_input == "3":
#     file_json = read_transactions_exl(data_file_path_exl)
#     result_user_three = filter_by_state(file_json, state_str)
#     print(result_user_three)
#
# user_input_sort = input("""Отсортировать операции по дате? Да/Нет
# """).lower()
#
# if user_input_sort == "да":
#
#     reverse = input("""Отсортировать по убыванию или возрастанию?
# """).lower()
#
#     if reverse == "убыванию":
#         reverse_str = True
#     elif reverse == "возрастанию":
#         reverse_str = False
#
#     if user_input == "1":
#         result_sort_one = sort_by_date(result_user_one, reverse_str)
#         print(result_sort_one)
#
#     elif user_input == "2":
#         result_sort_two = sort_by_date(result_user_two, reverse_str)
#         print(result_sort_two)
#
#     elif user_input == "3":
#         result_sort_three = sort_by_date(result_user_three, reverse_str)
#         print(result_sort_three)
#
#     else:
#         print("Некорректный выбор пользователя.")
#
# elif user_input_sort == "нет":
#     if user_input == "1":
#         print(result_user_one)
#     elif user_input == "2":
#         print(result_user_two)
#     elif user_input == "3":
#         print(result_user_three)
#
# user_input_currency = input("""Выводить только рублевые транзакции? Да/Нет
# """).lower()
#
# if user_input_currency == "да":
#     currency = "RUB"
#     if user_input == "1":
#         if user_input_sort == "да":
#             user_cur_one = list(filter_by_currency(result_sort_one, currency))
#         else:
#             user_cur_one = list(filter_by_currency(result_user_one, currency))
#         print(user_cur_one)
#
#     elif user_input == "2":
#         if user_input_sort == "да":
#             user_cur_two = list(filter_by_currency(result_sort_two, currency))
#         else:
#             user_cur_two = list(filter_by_currency(result_user_two, currency))
#         print(user_cur_two)
#
#     elif user_input == "3":
#         if user_input_sort == "да":
#             user_cur_three = list(filter_by_currency(result_sort_three, currency))
#         else:
#             user_cur_three = list(filter_by_currency(result_user_three, currency))
#         print(user_cur_three)
#
# else:
#     print("Некорректный выбор пользователя.")