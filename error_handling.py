#ERROR HANDLING
'''
Types of Errors
1.TypeError
2.IndexError
3.KeyError
4.ValueError
5.ZeroDivisionError
6.ModuleNotFoundError
......and much more(check documentation)

Syntax
try:
    ...
else:
    ...
except:
    ...
finally:
    ...
'''
try:
    a = int(input('What is your age?'))
    if a<0:
        raise Exception
    print(a)
except ValueError as v:
    print('please enter a number')
except Exception:
    print('please enter a valid age')
finally:
    print('Thank you!\n')

try:
    dict = {'a':1}
    x = input('Enter key')
    print(dict[x])
except KeyError:
    print('Enter a valid key')
finally:
    print('Thank you!')