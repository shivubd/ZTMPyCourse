#STRINGS

long_string='''
WWW
0 0
 ^
~~~
'''
print(long_string)

#string concatenation using '+'
name = 'SHIVARAJ'
print('Hello,'+' '+name+'!')
 
#formated strings 'f'
user='Shivaraj'
usn='2KL18CS122'
doy=2000
perc=93.76
print(f'\nMy name is {user}\nUSN is {usn}\nBirth year is {doy}\nAge is {2021-doy}\n10th Percentage is{perc}')
#type 2
print('\nMy name is {0}\nUSN is {1}\nBirth year is {2}\nAge is {3}\n10th Percentage is{4}'.format(user,usn,doy,str(21),perc))

#Escape sequences
print('\nHello I\'m Shivaraj,\nStudying Computer Science Engineering\nAge\tDOY \tPERC\n21 \t2000\t93.76\n')

#String indexes
Selfish = 'me me me'
print(Selfish)
print(Selfish[3])
print(Selfish[-1])
print(Selfish[1:4])
print(Selfish[:4])
print(Selfish[:])
print(Selfish[1::3])
print(Selfish[::-1])
print(Selfish[4:1:-1])

#len()
print('\nThe length of '+Selfish+' is '+str(len(Selfish)))
