'''
tuple is read only version of list
immutable
ordered
item assignment not possibe
indexing/ slicing possible
hetro/homo element can store inside a tuple
dulicates allwed
-if data is fixed and never change then we should go for tuple
'''
t=()
print(type(t))

t=(1,2,2,3,34)
print(type(t))
print(t)
#indexing/slicing possibe/slicing possible
print(t[0])
print(t[1])
print(t[2])
print(t[3])
print(t[4])
# print(t[5])  #IndexError: tuple index out of range


#item assignent not possible
# t[0]=2  #TypeError: 'tuple' object does not support item assignment 
#method of tuple

#len()
print(len(t))
#count()-number of occurance of element
print(t.count(2))

#index()-index of element
print(t.index(2))

#sored***

#min() max()
print(min(t))
print(max(t))


#del - delete entire tuple

'''
tuple faster than list
memory required in list compared to tuple is more
'''
t=((11,21,31),(11,21,33))
n=len(t)
for i in range(n):
    m=len(t[i])
    for j in range(m):
        print(i,j,t[i][j])

list=[1,2,3,4]
      