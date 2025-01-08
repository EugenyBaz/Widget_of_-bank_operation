import pytest
from freezegun import freeze_time
from src.decorators import log




def test_log():
    """ Тестирование работы функции через декоратор"""
    @log()
    def my_function(x, y):
        return x + y
    result = my_function(1, 2)

    assert result == 3

@freeze_time("2025-01-07 13:32:32.672206")
def test_print_log(capsys):
    """  Тестирование вывода в консоль при отсутсnвии файла filename"""
    @log()
    def my_function(x,y):
        return x + y
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out== ('my_function start: 2025-01-07 13:32:32.672206 '
                           'and end:2025-01-07 13:32:32.672206 result:3\n')


@freeze_time("2025-01-07 13:32:32.672206")
def test_print_log_str(capsys):
    """  Тестирование вывода в консоль при отсутсnвии файла filename
      и ошибки в передачи пустой строки вместо рагументов"""
    @log()
    def my_function(x,y):
        return x + y
    my_function("", 2)
    captured = capsys.readouterr().out.strip()
    expected_output = (f"my_function error: -type can only concatenate str (not \"int\") to str- Inputs: (1, 2), {{}} "
                       f"start: 2025-01-07 13:32:32.672206 and end:2025-01-07 13:32:32.672206 result:None\n").strip()
    assert captured == expected_output
