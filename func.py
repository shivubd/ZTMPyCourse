#Functions
#function defination
def add_val(num1,num2):         #num1,num2 here are POSITIONAL PARAMETERS
  print(num1+num2)
#function call
add_val(10,5)                   #num1,num2 here are ARGUMENTS

def divide_val(x,y=1):          #y is a DEFAULT PARAMETER with def val 1
  print(x/y)
divide_val(10,5)
divide_val(10)

def say_hello(name,emoji):
  print(f'Hello {name} {emoji}')
say_hello(emoji=':)',name='Shivaraj')#here name and emoji are KEYWORD ARGUMENTS

#return
def add_val_ret(num1,num2):
  return num1+num2
print(add_val(10,5))
print(add_val_ret(10,5))

def sum(num1,num2):
  def another_sum(n1,n2):
    return n1+n2
  return another_sum(num1,num2)
print(sum(110,90))
#print(another_sum(110,90)) cant run bcz of out of scope def

#Docstring
def mul(num1,num2):
  '''
  Info: Returns the product of param(num1) and param(num2)
  '''
  return num1*num2
help(mul)

def sum(tu):
  total=0
  for i in tu:
    total+=i
  return total

#*args 
def super_func(*args):         #*args here specifies multiple paramters
  return sum(args)
print(super_func(1,2,3,4,5,6,7,8,9))

#**kwargs
def super_func2(*args,**kwargs):
  tot=0
  print(kwargs.values())
  print(kwargs.keys())
  print(kwargs.items())
  for item in kwargs.values():
    tot+=item
  return sum(args)+tot
print(super_func2(1,2,3,4,5,n1=10,x=20,p=30))

#Rules if all types of parameters are to be specified
#(pos_params,*args,def_params,**kwargs)

#What is Scope?
print()
total=100
def disp():
  total=200
  print(total) #prints the total variable in the scope of disp func
disp()
print(total)   #prints the total variable in the global scope

#global
print()
total=199
def disp2():
  global total #takes the global total variable
  total+=1
  print(total)
disp2()

#nonlocal
print()
def outer():
  x='local'
  def inner():
    nonlocal x
    x = 'nonlocal'
    print('inner: ',x)
  inner()
  print('outer:',x)
outer()



