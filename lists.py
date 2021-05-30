#LISTS------------------------------------------------------------------------
li=['Shivaraj',9.5,8.5,7.7,8.82,8.32]

#List slicing
print(li[0])
print(li[0:3])
print(li[::-1])
print(li[5::-1])
print()

#Lists are mutable
li[0]='Shivu'
print(li)
print()

#Reference variable
li2=li
li2[1]='Deyannavar'
print(li2)
print(li)
print()

li3=li.copy()
li3[0]='SHIVARAJ'
print(li3)
print(li)
print()

#MATRIX
mat=[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
print(mat[2][1])
print(mat[1][2])
print()

#LIST METHODS------------------------------------------------------------------
#append()
lis=['Shivaraj',100,200,300,400,500]
lis.append('Deyannavar')
print(lis)
print()

#insert()
lis.insert(3,'xXx')
print(lis)
print()

#extend()
lis.extend([1,2,3])
print(lis)
print()

#pop()
x_var1=lis.pop(3)
x_var2=lis.pop()
print(str(x_var1)+' '+str(x_var2))
print(lis)
print()

#remove(val)
lis.remove(1)
print(lis)
print()

#index(val)
print(lis.index('Deyannavar'))
print(lis.index(400,1,5))
print()

#in keyword
print(400 in lis)
print('Dey' in lis)
print()

#count(val)
print(lis.count(400))
print()

#sort()
lit = [1,2,8,4,2,6]
lit.sort()
print(lit)
print()

#copy()
lit2=lit.copy()
print(lit2)
print(lit)
print()

#reverse()
lis.reverse()
print(lis)
print()

#join()
sentence = ['Hi,','I','am','Shivaraj','B','Deyannavar']
str1=' '.join(sentence)
print(str1)
print()

#clear()
lis.clear()
print(lis)
print()

#use of range() to create a list
print(list(range(1,5)))
print(list(range(10)))
print(list(range(10,1,-2)))
print()

#list unpacking
a,b,c,*other_elements,d,e=[1,2,3,4,5,6,7,8]
print(a)
print(b)
print(c)
print(other_elements)
print(d)
print(e)
print()
