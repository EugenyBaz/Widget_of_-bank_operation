import pytest
from src.processing import filter_by_state, sort_by_date

""" Тестирование фильтрации списка словарей по заданному статусу state"""


@pytest.fixture
def filter_dict():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize(
    "filter_dict, state_str, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        )
    ],
)
def test_filter_by_state(filter_dict, state_str, expected):
    assert (
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
        )
        == expected
    )

    """ Проверка работы функции с дефолтным значением state - должно быть отфильтровано по EXECUTED"""


@pytest.mark.parametrize(
    "filter_dict, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        )
    ],
)
def test_filter_by_state(filter_dict, expected):
    assert (
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
        == expected
    )

    """ Тестирование сортировки по дате """

@pytest.fixture
def sort_dict():
    return [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]

@pytest.mark.parametrize("sort_dict, reverse_str,expected",[
            (
                    [
                        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                    ], True,
                    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
            )
        ]
    )
def test_sort_by_date(sort_dict, reverse_str,expected):
    assert sort_by_date([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                    ],
                    True)== expected


def test_invalid_sort_by_date(sort_dict):
    with pytest.raises(ValueError):
        sort_by_date([{"id": 41428829, "state": "EXECUTED", "date": ""},
                        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                    ])

