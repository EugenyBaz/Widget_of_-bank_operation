import os
from typing import Union
from unittest.mock import MagicMock, Mock, patch

import dotenv

from src.external_second_api import convert_currency

dotenv.load_dotenv()
API_KEY = os.getenv("API_KEY")


def mocked_requests_get(*args: str) -> Union[Mock, None]:
    """ Функция мокирования запроса для имитации ответа от API"""
    if args[0].endswith("/USD"):
        mock_response = Mock()
        mock_response.json.return_value = {"conversion_rates": {"RUB": 101.1234}}
        return mock_response
    else:
        raise ValueError(f"Unexpected URL: {f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{"USD"}"}")


@patch("requests.get", side_effect=mocked_requests_get)
def test_convert_currency(mock_get: MagicMock) -> None:
    """ Функция проверки конвертации"""
    assert convert_currency("USD") == 101.1234
    mock_get.assert_called_once_with(f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD")
