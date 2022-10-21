#command prmpt- to command directly to the system


#pip(python inhancement package) -package manager for python to install python package.
'''
pip freeze- to show installed packeges in your system

'''


#command prompt command
'''
cd -change directory
cd..- return to previosed directory
mkdir-folder
google- command prmpt command-2
'''

#vs code-

#IDENTIFIERS
#VARIABLE-VARAIBLE USED TO STORE VALUE BUT IN PYTHON VARAIBALE ARE LIKE TAG TO AMEMORY LOCATION.

from ast import keyword


X=2
Y=2
print(id(X))
print(id(Y))
#rules to write varaible name
#1)name can not conbtain any special charecter  -!,@,#,$,^,&,*
#2)varaiable name can not be start with number
#3)we can not use any spcace in variable name
#4) a-z A-Z,0,9

rahul=10
#$achin
# 12rahul
######################################################################
'''
print-to print something
id-to get address of object
type - to check the data type of object
'''
#keyword/reserve word
import keyword
print(keyword.kwlist)

'''
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 
'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 
'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''
#operators
'''
arithmatic operaor-+,-,*,/,%,//,**
comparison or relational operarto-<,>,<=,>=,==,!=  :- logical i.e true or false
logical operator-and, or, not
assignment-  x+=5
membership operatort  - in , not in
identity operator-  is and  is not  - to check address
'''

#data types- data type defined type of data inside a varaiable
'''
mutable/ immutable
hetrigeneous/ homogeneouse
order/ unorder
indexing slicing
item assignment
'''
#all fundamental data type are immutable
'''
 int  x=2
  float  x=2.5
  complex  x=2+3J
  bool    X=True
  str   x='rahul '
'''

#list
'''
 order
 mutable
 item assignment possible
 duplicate allowed
  idexing/ slicing possible
   hetro/homo possible
'''

l=[1,22,3322,22,33,4,'rahul']
print(l[0])  #indeixng
print(l[0:4])  #slicing

l[0]= 'amol' #item assignment
#tuple
'''
 order
 immutable
 item assignment not possible
 duplicate allowed
  idexing/ slicing possible
   hetro/homo possible
'''

t=(1,2,2,33,4)

#set
'''
 mutable
unorder
 indexing/slicing not possible
duplicates not allowed
item assignment not possible
hetro/homo possible
insertion order not preserved
'''

#dict
'''
mutable
 key of dict is immutable and value can be anything
 key can not be repeted  value can be duplicate

'''

d={1:'amol',2:'rahul'}
print(d)
print(type(d))


#user input
# name=input('enter a nmae:-')
# print(name)

#by default user inpuit in a string format 
num1=int(input('eneter a num'))  #type cast string into num
print(num1)
print(type(num1))
x=10
print(num1+x)