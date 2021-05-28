#Dictionaries

my_dict = {'Name':'Shivaraj',10:93.76,12:82.6,(1,2,3,4):(9.5,8.5,7.71,8.81),}
#values can be of any type
#keys can be of only immutable types
print(my_dict)

#Dictionary methods
#print(my_dict[21])

#get()
print()
print(my_dict.get((1,2,3,4)))
print(my_dict.get(21))
print(my_dict.get('Name2','Key doesn\'t exists'))
print()

#dict()
di=dict(Name='Shivaraj',last='Deyannavar')
print(di)
print()

#keys()
print(my_dict.keys())
print('Name' in my_dict.keys())
print('(1,2,3)' in my_dict.keys())
print()

#values()
print(my_dict.values())
print((9.5,8.5,7.71,8.81) in my_dict.values())
print(11 in my_dict.values())
print()

#items()
print(my_dict.items())
print(('Name','Shivu') in my_dict.items())
print((12,82.6) in my_dict.items())
print()

#clear()
print(di)
di.clear()
print(di)
print()

#copy()
di = my_dict.copy()
di['Name'] = 'Shivu'
print(di)
print(my_dict)
print()

#pop()
x = my_dict.pop(10)
print(x)
print(my_dict)
print()

#popitem()
print(my_dict.popitem())
print()

#update()
my_dict.update({'Name':'Manjunath}'})
print(my_dict)
my_dict.update({10:93.76})
print(my_dict)
print()
