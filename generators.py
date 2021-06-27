#GENERATORS
def evenrange(num):
    for i in range(num):
        if i%2==0:
            yield i

for item in evenrange(20):
    print(item)