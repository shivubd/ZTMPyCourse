#DECORATORS
from time import time
def my_decorator(func):
    def wrap_func(*args):
        print('**********')
        func(*args)
        print('##########')
    return wrap_func
@my_decorator
def hello(name):
    print('Hellloooo '+name+' !')
hello('Shivaraj')

def performance(func):
    def wrapper(*args):
        t1 = time()
        func(*args)
        t2 = time()
        print(f'Sucessfully executed in {t2-t1}seconds')
    return wrapper

@performance
def test(n):
    for i in range(n):
        pass

test(10000000)
test(7000000)
