def multiply(n1,n2):
    try:
        return n1*n2
    except TypeError:
        return 'Enter only numbers'
def divide(n1,n2):
    try:
        return n1/n2
    except ZeroDivisionError:
        return 'Enter valid number'
    except TypeError:
        return 'Enter only numbers'