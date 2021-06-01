#Finding duplicates
li = ['a','b','b','c','e','d','e','d']
res=[]
for item in li:
  if li.count(item)>1:
    if item not in res:
      res.append(item)
res.sort()
print(res)
