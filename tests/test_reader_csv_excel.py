import json
from unittest.mock import patch, MagicMock
import pandas as pd
from io import StringIO
from src.reader_csv_excel import read_transactions_csv, read_transactions_exl
import csv


def test_read_transactions_csv() -> None:
    """ Проверка корректности чтения файлов csv"""
    test_data = [{"column1": "value1", "column2": "value2"}, {"column1": "value3", "column2": "value4"}]
    with patch('builtins.open', new_callable= MagicMock) as mock_open:
        """ Мокируем вызов open"""
        mock_file = mock_open.return_value
        mock_file.read.return_value = (
            'column1;column2\n'
            'value1;value2\n'
            'value3;value4\n'
        )

        mock_file.__enter__.return_value = StringIO(mock_file.read.return_value)
        """Используем StringIO для передачи данных в DictReader"""

        result = read_transactions_csv()
        assert result == test_data
        mock_open.assert_called()


def test_read_transactions_exl() -> None:
    """ Проверка корректности чтения файлов excel"""
    test_data = [{"column1": "value1", "column2": "value2"}, {"column1": "value3", "column2": "value4"}]
    with patch("src.reader_csv_excel.pd.read_excel",new_callable=MagicMock) as mock_read_excel:
        """ Мокирование вызова pd.read_excel на возвращаемый объект DataFrame """
        mock_read_excel.return_value = pd.DataFrame(test_data)

        result = read_transactions_exl("path_to_your_test_excel_file.xlsx")

        assert result == test_data

        mock_read_excel.assert_called()
