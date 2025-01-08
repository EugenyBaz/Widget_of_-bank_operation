import datetime
import os
from typing import Callable, Optional, Any


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NEW_BASE_DIR = os.path.dirname(BASE_DIR)


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор с принимаемыми аргументами"""

    def decorator(func: Callable) -> Callable:

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = datetime.datetime.now()
            """ Начало работы функции"""
            result = None
            try:
                """Прописываем через try и except выполнение функции с выводом результата в т.ч. ошибок"""
                result = func(*args, **kwargs)
                end_time = datetime.datetime.now()
                if filename:
                    log_file_path = os.path.join(NEW_BASE_DIR, "data", filename)
                    with open(log_file_path, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok start: {start_time} and end:{end_time} result:{result}\n")
                else:
                    print(f"{func.__name__} start: {start_time} and end:{end_time} result:{result}")
            except Exception as e:
                end_time = datetime.datetime.now()
                if filename:
                    log_file_path = os.path.join(NEW_BASE_DIR, "data", filename)
                    with open(log_file_path, "a", encoding="utf-8") as file:
                        file.write(
                            f"{func.__name__} error: -type {e}- Inputs: (1, 2), {{}}\n "
                            f"   start: {start_time} and end:{end_time} result:{result}\n"
                        )
                else:
                    print(
                        f"{func.__name__} error: -type {e}- Inputs: (1, 2), {{}} start: {start_time} "
                        f"and end:{end_time} result:{result}\n"
                    )
            finally:
                return result

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    """Декорируемая функция"""
    return x + y


my_function(1, 2)
