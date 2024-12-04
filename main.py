from src.masks import get_mask_card_number, get_mask_account

if __name__ == "__main__":
    number_card = input("Введите номер карты")
    print(get_mask_card_number(number_card))
    number_account = input("Введите номер счета")
    print(get_mask_account(number_account))
