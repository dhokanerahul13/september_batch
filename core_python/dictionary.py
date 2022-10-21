'''
mutable.
key of dict is immutable  value  can be anything.
key can not be repedtedor duplicate, value can be duplicate.
access values using keys.
inseryion order not preserved.
indexing and slicing concept not applicable.
'''

d={}   #s=set()-empty set
print(type(d))
#add item in dict /item assignmentusing key.
d[1]='rahul'
d[2]='malik'
d[3]='sagar'
d[4]='anushka'
d[5]='ankita'
print(d)
d={1: 'rahul', 2: 'malik', 3: 'sagar', 4: 'anushka', 5: 'ankita'}

#clear()-clear the dict and return empty dict
d.clear()
print(d)

#del-we can delete specific key value pair and entire dict also.
d={1: 'rahul', 2: 'malik', 3: 'sagar', 4: 'anushka', 5: 'ankita'}
del(d[1])
print(d)

#len()-lenth of dict shoe
print(len(d))

#pop(key)-pop return perticular value from dict

print(d)
print(d.pop(5))
print(d)

#popitem()-remove and return last element from dict
print(d.popitem())
print(d)

d={1: 'rahul', 2: 'malik', 3: 'sagar', 4: 'anushka', 5: 'ankita'}

#keys()-return alll keys
print(d.keys())

#values-return ALLL VALUES FROM A DICT
print(d.values())

#items()-it returns list of tuples represeting keyt and vALUE PAIR
print(d.items())


#########################################################################
d={1: 'rahul', 2: 'malik', 3: 'sagar', 4: 'anushka', 5: 'ankita'}

for i,j in d.items():
    # print(i)
    print(i,j)

###########################################################################
# setdefault(key,value)-add    
d={1: 'rahul', 2: 'malik', 3: 'sagar', 4: 'anushka', 5: 'ankita'}
d.setdefault(6,'amol')
print(d)

#update()-update the existing element if the element not found than it will to it
x={11:'rakhi',2:'rajiv'}
print(d.update(x))
print(d)
##########################################################################


