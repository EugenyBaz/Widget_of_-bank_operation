from src.widget import mask_account_card, get_date

if __name__ == "__main__":
    number_card = input("Введите номер карты или счета")
    print(mask_account_card(number_card))

    date= input("Введите дату")
    print(get_date(date))
