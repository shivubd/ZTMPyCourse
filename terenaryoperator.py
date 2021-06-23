#Terenary operator
is_Friend = bool(int(input('Is he your friend\nOption: 1(Yes) 0(No) ')))
res = 'Message allowed'if is_Friend else'Messages not allowed'
print(res)
