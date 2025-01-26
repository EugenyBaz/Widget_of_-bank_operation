import json
from unittest.mock import patch
import pandas as pd
from src.reader_csv_excel import read_transactions_csv, read_transactions_exl


def test_read_transactions_csv() -> None:
    """ Проверка корректности чтения файлов csv"""
    test_data = [{"column1": "value1", "column2": "value2"}, {"column1": "value3", "column2": "value4"}]
    with patch("src.reader_csv_excel.pd.read_csv") as mock_read_csv:
        """ Мокирование вызова pd.read_csv на возвращаемый объект DataFrame """
        mock_read_csv.return_value = pd.DataFrame(test_data)

        result = read_transactions_csv()

        assert result == json.dumps(test_data, ensure_ascii=False)

        mock_read_csv.assert_called()


def test_read_transactions_exl() -> None:
    """ Проверка корректности чтения файлов excel"""
    test_data = [{"column1": "value1", "column2": "value2"}, {"column1": "value3", "column2": "value4"}]
    with patch("src.reader_csv_excel.pd.read_excel") as mock_read_excel:
        """ Мокирование вызова pd.read_excel на возвращаемый объект DataFrame """
        mock_read_excel.return_value = pd.DataFrame(test_data)

        df = pd.read_excel(read_transactions_exl)

        result = read_transactions_exl(df)

        expected_result = json.dumps(test_data, ensure_ascii=False)

        assert result == expected_result

        mock_read_excel.assert_called()
