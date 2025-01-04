import datetime

def log (filename="mylog.txt"):

    def decorator(func):

        def wrapper(*args, **kwargs):
            start_time = datetime.datetime.now()
            result= func(*args, **kwargs)
            end_time = datetime.datetime.now()
            print(f"{func.__name__} start: {start_time} and end:{end_time} result:{result}")
            return result
        return wrapper

    return decorator





@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)