for item in 'Zero to Master':
  print(item)
print()
for item in [1,2,3,4,5]:
  print(item)
print()
for item in (1,2,3,4,5):
  for a in ['a','b','c','d','e']:
    print(item,a)
print()
user = {'name':'shivu','perc':93.76,(1,2,3):[9.5,8.5,7.71]}
# in dictionaries the keys can be only of immutable type
for item in user:
  print(item)
print()
for item in user.keys():
  print(item)
print()
for item in user.values():
  print(item)
print()
for item in user.items():
  print(item)
print()
for k,v in user.items():
  print(k,v)
print()
