import datetime
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NEW_BASE_DIR = os.path.dirname(BASE_DIR)
def log(filename=None):

    def decorator(func):

        def wrapper(*args, **kwargs):
            start_time = datetime.datetime.now()
            result = None
            try:
                result= func(*args, **kwargs)
                end_time = datetime.datetime.now()
                if filename:
                    log_file_path = os.path.join(NEW_BASE_DIR, 'data', filename)
                    with open(log_file_path, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok start: {start_time} and end:{end_time} result:{result}\n")
                else:
                    print(f"{func.__name__} start: {start_time} and end:{end_time} result:{result}")
            except Exception as e:
                end_time = datetime.datetime.now()
                if filename:
                    log_file_path = os.path.join(NEW_BASE_DIR, 'data', filename)
                    with open(log_file_path, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: -type {e}- Inputs: (1, 2), {{}}\n "
                                   f"   start: {start_time} and end:{end_time} result:{result}\n")
                else:
                    print (f"{func.__name__} error: -type {e}- Inputs: (1, 2), {{}} start: {start_time} and end:{end_time} result:{result}\n")
            finally:
                return result

        return wrapper
    return decorator



@log()
def my_function(x, y):
    return x + y

my_function("",2)
