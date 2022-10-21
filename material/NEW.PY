'''
cmd
pip
intro
uses
features
-identifiers-
we can not strat with num,
special char not allowed excpt underscore-@,#,$,%,^,&
spaces not allowed 
###################################################################################
-comments
-variable
Rahul$12=12 -special charecter
###################################################################
-keyword/reserved word
-operators
1)arthmatic-+.-.*,/,//,%,**
2)comarison or relatinal operator:-> <,>,<=,>=,!=,==,output n boolean
3)logical operator:->and,or,not-->output n boolean
4)assignment
x=2
x=x+2
x+=2  -->
x=x*2  -->x*=2

5)membership opeartot  in , not in
6)identity operator-->is ,is not
7)bitwise**
8)ternary operator**
is and == differance
########################################################################################################

-data types-data type represent type of data inside a varable.- must read theory about this.
#mutable vs immutable*
#hetro vs homo
#order vd unorder
#insertion order preserved
#WHAT IS COLLECTION
#WHAT IS SEQUENCE
#

flow control
'''

#data types
#int
x=2
print(type(x))
print(id(x))
#flaot
x=2.0
print(type(x))
print(id(x))

#complex
x=2+3j
print(type(x))
print(id(x))

#4)boolean num
x=True
print(type(x))
print(id(x))
#################################################################################
#5)String
x='hello'
print(type(x))
print(id(x))
'''
IMMUTABLE
INSERTION PRESERVED
INDEXING/SLICING POSSIBLE
ITEM ASSIGNMENT NOT POSSIBLE
'''
#STRING FOLLOW POSITIVE AS WELL AS NEGATIVE INDEXIBNG
x='hello'
#without index
for i in x:
    print(i)

#with index
for i in range(len(x)):
    print(x[i],i)  #slice of string

#method of string
'''
replace,reaverse,split,find,format,index,count,case related method,check type of char method,
'''    
x='hello'
y=x.replace('h','r')  #replace will make other object
print(y)

#foramatting of string
#1)noramal comma seperated way
#2)F STRING METHOD
#3)FORMAT METHOD

################################################################################