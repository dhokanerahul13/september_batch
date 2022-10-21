'''
#numpy 
numpy is python numerical libraray.
it provide mechanism to store multi d array.
numpy can stor hetro+homo eleemnt
mutable
indexing/slicng possible
item asignment ossible
faster than list, tupe,set, and inbuilt array module



#pandas

used to create dataframe.
panadas +numpy+matplotlib=matlab

#numpy is third party packges

pip install numpy
'''

import numpy #this will import entire numpy module

from numpy import*  # this will import all classes,objects,varaibel from n umpy

#creating one -d array using numpyt 

import numpy
list=numpy.array([11,22,33,44,'amol',[11,22,33]])
print(list)
print(id(list))
print(type(list))

#specific data type
list=numpy.array([11,22,33,44],dtype=int)
print(list)
print(id(list))
print(type(list))


#indexing /slicing
print(list[0])
print(list[1])
print(list[2])
print(list[3])

#item assignmment poissible
list[0]=1111
print(list)


'''
list-if you  want group of element of differant  dtaatype and you  canchange the content
then we shoul dgo for list.

set-
if we want group of element of same or diferent data type where order is not matter
then we shold go for set.

tuple-if we want orderder  group of element of same/fiffrent data type where we are 
not suppose to change the eement then we should go for tuple.


numpy array-if you  want group of element of differant  dtaatype and you  canchange the content
then we shoul dgo for list. here dtaa not in small amount.

dict
-if we want group of element with key value pair then we should go for dictinary.
'''

from numpy import*

student=array([11,22,33,44,55])
print(student)
for element in student:
    print(element)

#with index
for element in range(len(student)):
    print('index:-',element,'element:-',student[element])
print('###################################################')
#while loop
n=len(student)
i=0
while i<n:
    print('index:-',i,'element:-',student[i])  
    i+=1 

#ways of creating numpy 1-d array
'''
logspace
lenspace
arrange
zeroes
once
reshape
'''    

#stack
#queue
#sorting in python
'''
bubbble sort
slection sort
insertion sort
'''

#searching
'''
binary search
linera search
'''

#waysof crating multi-d array
'''
array
zeroes
ones
reshaps
'''

#reshape()-
#convertoing multi d to 1-d array
a=array([[1,2,3],[1,2,3],[1,2,3]])
b=reshape(a,(9))
print(b)

#1-d to 2-d
arr=array([1,2,3,4,5,6,7,8,9,11,22,33])
newarr=reshape(arr,(3,4))
print(newarr)

arr=array([1,2,3,4,5,6,7,8,9,11,22,33,33,44,22,55,66,77])
newarr=reshape(arr,(2,3,3))
print(newarr)

#flattening the array
'''
flattning of array means  convering multi d arry into 1d aray
'''

a=array([[1,'amol','8923725'],[2,'lalit','78234'],[3,'rushi','578234']])
newarr=reshape(a,(-1))
print(newarr)
print(a.flatten)
print(a)

###########################################
#joining array using stack fucntion sarrtack()
'''
stacking is same as concatinsation , the one differance is that stacking is done only along new axis.
'''
import numpy as np
array1=np.array([1,2,3,4])
array2=np.array([1,223,3,4])
arr=np.stack((array1,array2))
print(arr)

#multiple array combine
array1=np.array([1,2,3,4])
array2=np.array([1,223,3,4])
array3=np.array([112,22,33,44])
arr=np.stack((array1,array2,array3))
print(arr)


#stacking along rows
#numpy provide helper function hstack() to stack along rows
import numpy as np
array1=np.array([1,2,3,4])
array2=np.array([1,223,3,4])
arr=np.hstack((array1,array2))
print(arr)


array1=np.array([1,2,3,4])
array2=np.array([1,223,3,4])
array3=np.array([112,22,33,44])
arr=np.hstack((array1,array2,array3))
print(arr)

#stacking along column
#vstack()
import numpy as np
array1=np.array([1,2,3,4])
array2=np.array([1,223,3,4])
arr=np.vstack((array1,array2))
print(arr)


array1=np.array([1,2,3,4])
array2=np.array([1,223,3,4])
array3=np.array([112,22,33,44])
arr=np.vstack((array1,array2,array3))
print(arr)

##########################################################################
#split() function**
arr=np.array([11,22,33,44,55,66,77,88])
newarr=np.split(arr,(2,2,2))
print(newarr)

#splliting multi-d array
print('#####################################################')
arr=np.array([[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2]])
newarr=np.split(arr,4)
print(newarr)

print('######################################')
#searching arrays   with#whaere
import numpy as np
arr=np.array([1,2,23,3,4,'3',3,5,6,3,3,3])
x=np.where(arr=='3')
print(x)


arr=np.array([11,22,33,44,55,66,77,88])
arr1=np.where(arr%2==0)
print(arr1)

#########################################################
'''
data=piece of inforamation
database-collection of data.
dbms(database management syytem)
RDBMS(relatinal database management syytem)-mysql,oracle,postgresql,mariadb-is in the form of table
sql(structure querry languuage)-to querry over rdbms

'''