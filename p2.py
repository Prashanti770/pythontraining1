
"""i=0
while i<11:

    print(i)
    i += 2
"""
list1=[1,2,3,4,2,2]
list2=['a','v','c','d']
list3=["avzxbc","daaaaaaaaafg","tuv"]
print(min(list1))
print(max(list2))
list1.append(9)
print(list1)
list2.append('e')
print(list2)

print(list1.count(2))
list1.insert(0,8)
print(list1)



list1.remove(9)
print(list1)

list1.pop(0)
print(list1)
tup4=tuple(list3)
print(tup4)
print(type(tup4))

dict1={'a':22,'b':23,'c':34}
print(dict1['a'])
dict1['d']=44
print(dict1)
#print(dict1.popitem())
print(dict1.pop('b'))
print(dict1)
print(dict1.get('d'))