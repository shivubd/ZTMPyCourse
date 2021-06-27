#FILE I/O
#Creating a file object
my_file = open('text.txt','r')

#Reading from a file
print(my_file.read())
my_file.seek(0)
print(my_file.readline())
print('next line')
print(my_file.readline())
my_file.seek(0)
print(my_file.readlines())
my_file.close()

#Writing to a file
with open('test.txt','w') as my_file:
    text = my_file.write('Hello, world!')
    print(text)

#appending to file
with open('test.txt','a') as my_file:
    print(my_file.write('\nMy name is shivaraj.'))

#Opening a file in both read and write mode
with open('test.txt','r+w') as myf:
    pass
