set1={'abc','bde'}
set2={0,9,8,7}
set1.add('jkl')
print(set1)
set2.add(5)
print(set2)
set2.remove(0)
print(set2)
set2.discard(9)
print(set2)
set1.pop()
print(set1)
set3 =set1.union(set2)
print("combine",set3)
set1.add('opi')
set1.update(set2)
print(set1)