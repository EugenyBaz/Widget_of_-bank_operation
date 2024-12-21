from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date

if __name__ == "__main__":

    number_card = input("Введите номер карты")
    """Вывод номера карты в скрытом виде"""

    print(get_mask_card_number(number_card))

    number_account = input("Введите номер счета")
    """Вывод номера счета в скрытом виде"""

    print(get_mask_account(number_account))



if __name__ == "__main__":
    number_card = input("Введите номер карты или счета")
    print(mask_account_card(number_card))

    date= input("Введите дату")
    print(get_date(date))


if __name__ == "__main__":

    state = input ("Введите статус")
    state_str = state.upper()

    print(
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ], state_str
        )
    )

if __name__ == "__main__":

    reverse = input("Введите порядок сортировки True(сначала новые) или False(сначала ранние)")
    reverse_up= reverse.title()
    if reverse_up == "True":
        reverse_str = True
    else:
        reverse_str = False


    print(
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED","date":"2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ], reverse_str
        )
    )
