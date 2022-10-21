'''
array is an object that provide mechnism for stoting multiple element inside a single variable.
array is befivial if you want to store group of element of same data type.
mutable
item assignmnet possible
indexing slicing ok
hetro eement not possible
'''

import array
#way:-1
student=array.array('i',[11,22,33,44,55])
#syntax
#arrayobject=modulename.classname('typecode',[elements])
print(id(student))
print(type(student))
print(student)
#way:-2
from array import*
student=array('i',[11,22,33,44])
print(id(student))
print(type(student))
print(student)


#modifing inbuilt array function
student[1]=44
print(student)

#for loop without index

for i in student:
    print(i)

#for loop with index
for i in range(len(student)):
    print(i,student[i])

#types of arrya
'''
one-d array-single row and multiple columns.
i.e
student=array.array('i',[11,22,33,44,55])
 
multi-d array
student=array.array('i',[111,22,3,,4],[11233,4,4,3,5,5] )
'''    

#canb we store string value inside array inbuilt module how???

#appnd()
student=array('i',[11,22,33,44])
print(student.append(444))
print(student)
#insert()
print(student.insert(3,555))
print(student)

#pop()

print(student.pop())
#pop(n)-spcific element
print(student)
print(student.pop(0))

#remove()
print(student.remove(555))
print(student)
#index()
print(student.index(44))
print(student)
#reverse()
student.reverse()
print(student)


#user inut by your self


#
