

import time

def log (filename="mylog.txt"):

    def decorator(func):

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    return decorator





@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)