from unittest.mock import patch
import pandas as pd
import json

from src.reader_csv_excel import read_transactions_csv, read_transactions_exl


def test_read_transactions_csv():
    test_data = [
        {'column1': 'value1', 'column2': 'value2'},
        {'column1': 'value3', 'column2': 'value4'}
    ]

    # Подмена вызова pd.read_csv на возвращаемый объект DataFrame
    with patch('src.reader_csv_excel.pd.read_csv') as mock_read_csv:
        mock_read_csv.return_value = pd.DataFrame(test_data)

        result = read_transactions_csv()

        expected_result = json.dumps(test_data, ensure_ascii=False)

        assert result == expected_result

        mock_read_csv.assert_called()


def test_read_transactions_exl():
    test_data = [
        {'column1': 'value1', 'column2': 'value2'},
        {'column1': 'value3', 'column2': 'value4'}
    ]

    # Подмена вызова pd.read_csv на возвращаемый объект DataFrame
    with patch('src.reader_csv_excel.pd.read_excel') as mock_read_excel:
        mock_read_excel.return_value = pd.DataFrame(test_data)

        df = pd.read_excel(read_transactions_exl)

        result = read_transactions_exl(df)

        expected_result = json.dumps(test_data, ensure_ascii=False)

        assert result == expected_result

        mock_read_excel.assert_called()