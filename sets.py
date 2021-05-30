#Set methods
st = {1,2,3,4,4,5}
print(st)
print()

#Set methods
st1 = {1,2,3,4,5}
st2 = {4,5,6,7,8,9,10}

#differene()
print(st1.difference(st2))
print(st2.difference(st1))
print()

#discard()
st.discard(1)
print(st)
print()

#difference_update()
print(st)
st.difference_update(st2)
print(st)
print()

#intersection()
print(st1.intersection(st2))
print(st1 & st2)
print()

#union()
print(st1.union(st2))
print(st1 | st2)
print()

#isdisjoint()
t1 = {1,2,3}
t2 = {4,5,6}
t3 = {1,2,3,4,5,6}
print(t1.isdisjoint(t2))
print(t1.isdisjoint(t3))
print()

#issubset()
print(t1.issubset(t2))
print(t1.issubset(t3))
print()


