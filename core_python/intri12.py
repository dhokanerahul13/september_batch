#list
'''
orderd
mutable
dulicate allowed
home/hetro data save
item assignment possible
indexing/slicing possible
'''

l=[1,2,2,'amol',4]
#indexing
print(l[0])
print(l[1])

#item assignment

l[0]='sagar'
print(l)


#tuple
'''
immutable
read only version of list
 item assignmnet not ossible
 duplcate allowed
  hetyro/ homo possbile data posssible
  indesing/ slicing possible
'''

t=(11,22,33,33,'april')

# t[0]='amol'


#set
'''
mutable
unorder-insertion order not preserved
 indexing/ slicing not possible
 duplicates not allowed
 hetro/homo possible
 item assignment not possible

'''
s={1,2,2,5,'amol'}
print(s)
# print(s[0])
# s[0]=6


#dictinary
'''
key valu pair/ mapping
key must be immutable / value can be anything
key can not be duplicates  value can be

'''

d={1:'sagar',2:'amol',3:'dnyana',4:'rajat'}
print(d[1])

#range()-immutable - to generate perticualr range

s=range(10)
print(s)
print(type(s))