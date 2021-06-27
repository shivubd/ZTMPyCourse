#MODULES EXAMPLE
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    try:
        return n1/n2
    except ZeroDivisionError:
        return 'Enter a valid nunber'
