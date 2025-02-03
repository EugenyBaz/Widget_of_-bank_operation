
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ""))
data_file_path = os.path.join(project_root, "data", "transactions.csv")
data_file_path_exl = os.path.join(project_root, "data", "transactions_excel.xlsx")
data_file_path_json = os.path.join(project_root, "data", "operations.json")

result_user_one = None
result_user_two = None
result_user_three = None

if user_input == "1":
    with open(data_file_path_json, 'r', encoding= "utf-8") as file:
        trans_list_conv = json.load(file)
    result_user_one = filter_by_state(trans_list_conv, state_str)
    print(result_user_one)

elif user_input == "2":
    file_json = read_transactions_csv(data_file_path)
    result_user_two = filter_by_state(file_json, state_str)
    print(result_user_two)

elif user_input == "3":
    file_json = read_transactions_exl(data_file_path_exl)
    result_user_three = filter_by_state(file_json, state_str)
    print(result_user_three)

user_input_sort = input("""Отсортировать операции по дате? Да/Нет
""").lower()

if user_input_sort == "да":

    reverse = input("""Отсортировать по убыванию или возрастанию?
""").lower()

    if reverse == "убыванию":
        reverse_str = True
    elif reverse == "возрастанию":
        reverse_str = False

    if user_input == "1":
        result_sort_one = sort_by_date(result_user_one, reverse_str)
        print(result_sort_one)

    elif user_input == "2":
        result_sort_two = sort_by_date(result_user_two, reverse_str)
        print(result_sort_two)

    elif user_input == "3":
        result_sort_three = sort_by_date(result_user_three, reverse_str)
        print(result_sort_three)

    else:
        print("Некорректный выбор пользователя.")

elif user_input_sort == "нет":
    if user_input == "1":
        print(result_user_one)
    elif user_input == "2":
        print(result_user_two)
    elif user_input == "3":
        print(result_user_three)

user_input_currency = input("""Выводить только рублевые транзакции? Да/Нет
""").lower()

if user_input_currency == "да":
    currency = "RUB"
    if user_input == "1":
        if user_input_sort == "да":
            user_cur_one = list(filter_by_currency(result_sort_one, currency))
        else:
            user_cur_one = list(filter_by_currency(result_user_one, currency))
        print(user_cur_one)

    elif user_input == "2":
        if user_input_sort == "да":
            user_cur_two = list(filter_by_currency(result_sort_two, currency))
        else:
            user_cur_two = list(filter_by_currency(result_user_two, currency))
        print(user_cur_two)

    elif user_input == "3":
        if user_input_sort == "да":
            user_cur_three = list(filter_by_currency(result_sort_three, currency))
        else:
            user_cur_three = list(filter_by_currency(result_user_three, currency))
        print(user_cur_three)

else:
    print("Некорректный выбор пользователя.")



