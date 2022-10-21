#operators=operators is A SYMBOL THAT PERFORM  CERTAIN OPERATIONS
#TYPES OF OPERATES
'''
1)ARITHMATIC OPERATORS
2)RELATINAL OPERTOR OR COMPARISON
3) LOGICAL OPERATOR
4)ASSIGNMENT OPERTOR
5)MEMBERSHIP
6) IDENTITY
7)BITWWISE OPERAORS
'''

#1) ARITHMATIC OPERATOR:-} +,-,*,/,%,//,**
a=16
b=10

print(a+b) # addotion  #add two numbwr
print(a-b) #substarction #sub two num
print(a*b) # multipliocation #MULTI TWO NUM
print(a/b)  #division  #DIVISION
print(a//b)  #floor divisaion  #WHOLE VALUE OF DIVISION
print(a%b) #modulo operator  #REMINDER
print(a**b)  #exponant or power  #POWER OF PERTICULAR NUM


#2)REALATINAL OPERATOR  >,<,>=,<=,==,!=  #output always in logical
a=10
b=20

print(a>b)
print(a<b)
print(a==b)


#3)logical  operartor  and,or,not( logical output must be in logical form i.e true and flase)

#and= if any of the condition is flase whole  outut will false.
# or=if any of the condition is true then whole condition is true
# not=complimewnt or invert

print(a>b or a<b)
print(a>b and a<b)
print( not a>b)


#4)assignment operator
# a=a+1  #a+=1
# a=a-1  #a-=1
# a=a*1  #a*=1

a=10
a+=10  #a=a+1-10
print(a)

a-=10   #a=a-10
print(a)

#5)membership operator= in and not in( always throgh logical true or false)
s='today is good day but i wake up early'
print('good' in s )

l=[11,22,3,3,4,4,5]
print(22 in l)


#6) identity opeartors  = is and is not ( always throgh logical true and fase as output)

c=20
b=20

print(a is b)
print(a == b)


#differance between == and is operator******


############################################################################
#type casting / type conversion
'''
  conversion of one data type ino another is called type casting
'''

a=10
print(float(a))
print(list(a))