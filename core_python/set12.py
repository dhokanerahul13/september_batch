'''
unorder
unique/ duplicates are not allowed
indexing and slicing not possible
item assignment not possible
hetrogeneoue and homogeneous data possible
mutable
'''
s=set()
s={10,20,30,40,50}
print(s)
print(type(s))
#indexing and slicing not possible
# print(s[0])  #TypeError: 'set' object is not subscriptable

#item assignment not possible
# s[0]=5#TypeError: 'set' object does not support item assignment 

########################################################################

#methods of set
#add()
s=set()
print(s.add(10))
print(s.add(20))
print(s.add(30))
print(s.add(40))
print(s.add(50))
print(s)

#update-to add multiple item to the set
l=[100,200,300]
print(s.update(l))
print(s)

#copy()-if we changw thw contwnt in copy it willl changw the object
s1=s.copy()
s1.add(14)
print(id(s))
print(id(s1))


#aliasing / assigning-if we assign value in set then, if we make any changes in any
#one object that will reflect on other object.
m=s1
m.add(17)
print(id(m))
print(id(s1))


#pop()-remove and return last element from a a set.
s={10,20,30,40}
print(s.pop())
print(s)

#remove()-remove specific element if element not found than it will through error
print(s.remove(10))
print(s)

#discard()-remove specific element if element not fount than it wont through any error
print(s)
print(s.discard(20))

#clear=remove element from a set
print(s)
print(s.clear())
print(s)


#mathematical operations on set
#union()-COMBINE TO SET
s={1,2,3,4}
s1={11,22,33,3,4}
print(s.union(s1))
x=s.union(s1)
print(x)

#intersection-returen common selement from set
print(s.intersection(s1))

#differrence-return the element that are present in first set but not preset in second.
s={1,2,3,4}
s1={11,22,33,3,4}
print(s1.difference(s))

#membership
print(1 in s)
print(11 in s1)


#set as a user input
n=int(input('enter a number of element that you want tyo insert in set:-'))
s=set()
for i in range(n):
    s.add(int(input('enter a element')))
print(s)    


#assignment
s={{1,2,3},1,2,3,'rahul',[1,2,3,4]}