#check srtring method that changes content of string
'''
collection of element inside a square bracket
MUTABLE
INDEXING/ALICINGH POSSIBLE
ORDERED
ITEM ASSIGNMENBT POSSIBLE
DUPLICATES ALLOWED
HOMOGENEOUE+HETROGENEOUS ELEMENT ARE ALOWED
- list is used where you wnat to make changes in your list frequently.

'''

from telnetlib import PRAGMA_HEARTBEAT


l=[1,2,3,"welcome",4,5,6,7]
print(l)
print(type(l))
print('before changing',id(l))
#indexing slicing possible
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])
print(l[5])

print(l[0:10])
#item assigenment
l[6]='lalit'
print('after chang',id(l))
print(l)

#len()-find the length of list
print(len(l))

#membership
print('lalit' in l)
########################################################################################
#add element in list 
#append()- add element at the last of list
list1=[1,2,2,3,4,54,5]
print(list1.append('dnyana'))
print(list1)

#insert-insert item at specified index-insert(index,element to insert)
print(list1.insert(4,'amol'))
print(list1)

#extend()-add any iterable item into a list
list2=[1,2,3,4,5]
list3=[1,2,3,4,5]
print(list2.extend(list3))
print(list2)
print(list3)
#######################################################################################
#TAKING USER INPUT AS A LIST
# n=int(input('enter a number of element you want to insert inside a list:-'))
# list4=[]
# for i in range(n):
#     element=input('enter a element')
#     list4.append(element)
# print(list4)    

###########################################################################################
#remove list element
fruits=['banana','cherry','apple','orange','mango','grapes']
#1)pop()-remove  and returm last element of list
print(fruits.pop())
print(fruits)

#2)del-pythom inbuilt function
# del fruits     
print(fruits) #this will through name error because it delete entire list


#3)clear()-clear list element
# print(fruits.clear())
print(fruits)

#4)remove-remove the specific element
fruits.remove('cherry')
########################################################################################
#sort()
print(fruits.sort(reverse=False))
print(fruits)

#copy
x=fruits.copy()
print(x)

#######################################################################
#loop through list element
#without index
for i in fruits:
    print(i)


#with index
for i in range(len(fruits)):
    print('list element index',i,'elements are:-',fruits[i]) 
############################################################################################
#assign vs copy

#1)ASSIGN VALUE OF LIST TO OTHER VARIABLE-it will reflect changes on assign variable after
#changling current variablle data
X=[1,2,3,4,5]
Y=X
print(Y)
Y[0]=40
print(Y)
print(X)
print(id(x))
print(id(Y))  #same id

#2)copy-while coping
x=[1,2,3,4,5]
z=x.copy()
z[2]=44
print(x)
print(z)
print(id(x))  #different id after copy list
print(id(z))

#= meant of aliasing or assigning
#copy- meant for cloning

#######################################################################################


#reverse()=can reverse the order of list
n=[1,2,3,4]
print(n.reverse())
print(n)

###################################################################################################
#nested list- list inside  list
a=[1,2,3,4,[1,12,234,3]]
print(a)
print(id(a))
print(type(a))
#indexing and slicing
print('##################################################')
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4][0])
print(a[4][1])
print(a[4][2])  #index  ,outer index, inner value
print('##################################################')
#acccess nested list usingn for loop\
for i in range(len(a)):
    if type(a[i])==list:
        for j in range(len(a[i])):
            print(i,j,a[i][j])
    else:
        print(i,a[i])        
#################################################################################
#mutable vs immutable*
#hetro vs homo
#order vd unorder
#insertion order preserved
#WHAT IS COLLECTION
#WHAT IS SEQUENCE       
# acccess  this with inner and outerb index
# x=[[1,2,3],[1,2,3] ] -try own at home


