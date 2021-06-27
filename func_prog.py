#FUNCTIONAL RPOGRAMMING

#map() function
def multiplyby2(i):
    return i*2
print(list(map(multiplyby2,[1,3,5,7,9])))

#filter() function
def check_odd(i):
    return i%2!=0
print(list(filter(check_odd,[1,2,3,4,5,6,7,8,9,0])))

#zip() function
my_list = [1,2,3]
your_list = (10,20,30)
their_list = {100,200,300}
print(list(zip(my_list,your_list,their_list)))

#reduce() function
my_list = [1,2,3]
def accumulator(acc,item):
    print(acc,item)
    return acc+item
#print(reduce(accumulator,my_list,0))

#lambda expressions
my_list = [1,3,5,7,9]
print(list(map(lambda i:i*2,my_list)))

#list/tuple/set comprehension
my_list = [x*2 for x in range(10)]
print(f'here: {my_list}')
