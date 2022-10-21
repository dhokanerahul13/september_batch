'''
if group of statment repetadly recuired thane it is not recommanded to write it every time
we have to fedine this statment as a single unit and we can call that unit as manay as time yoy want

function is a block of code that we can call when it requiesd,

advantages:-
code reusability.
#their are two types of function
1)BUILT IN FUNCTIION
THE FUNCTION WHICH COME ALONG WITH PYTHON SOFTWAREAUTOMATICALLY ARE CALLED BUILTINT
FUNCTION.  I.E LEN(),PRINT(),ID(),TYPE().

2)USER DEFINED FUNCTION.

THE FUNCTION WHICH ARE DEVLOPED BY PROGRAMMER EXPLICITLY ACCORDING TO BUSINESS LOGIC ARE CALLED
USER DEFINED FUNCTION.

def function_name():
    stATAMENTS

'''
#WITHOUT ANY ARGUMENT



def hello():  #functiohn defihne
    print('hii how are you') #statement of dfunctions
hello()  # function calling    



#FUNCTION WITH ARGUMENT
def sum(a,b): #function define
    print(a+b)  #function ogc
sum(1,2)   #function calling


#parameter are input to the function .
#if a function contains parameter then at the time of calling we should compolsory 
# [ass value oterwise it will throgh erroe]
print('#####################################################')

# def even_num(a):
#     if a%2==0:
#         print('the number is even')
#     else:
#         print('number is odd')
# a=int(input('enter a nnumber:-'))
# even_num(a)            


#return-it only return the logic of functon .return only evalute funtion not printing the evaluate value
print('###########################################################')
# def even_num(a):
#     if a%2==0:
#         return'the number is even'
#     else:
#         return 'number is odd'
# a=int(input('enter a nnumber:-'))
# x=even_num(a)
# print(x)    



#  differance return vs print

####################################################################

#types of argument
def sum(a,b):   #foramal argumernt
    print(a+b)
sum(1,2)  #actual argument

#formal argument-function defining argument are called formal argumnet.
#actual argument-functin calling argumnet are called actual argument.


#types of actual argument

'''
1)positinal argumnet
2)keyword argumnet
3)default argument
4)varaiable lemgth
5)keyword variable lenth
'''
#1)positiinal argument-the argument which are pass at the correct positin
def sum(a,b):   #foramal argumernt
    print(a+b)
sum(1,2)  #actual argument
print('################################################')
#2)keyword argument
def sum(a,b):   #foramal argumernt
    print(a+b)
sum(a=1,b=2)  #actual argument
print('#########################################')
#3)default argument
def sum(a,b=5):   #foramal argumernt
    print(a+b)
sum(a=1) 

print('############################################################')

#4)varaiable length argujent
def sum(*a):   #foramal argumernt#multiple value pass 
    print(a)
    for i in a:
        print(i)
sum(11,22,33,44,550)
print('##################################################')
#5)keyword varaiable length argument #kwargs

def dispaly(**k):
    print(k)
    
dispaly(name='rahul',salary=968)  

##########################################
# def dispaly(**k):
#     print(k)
# name=input('enter a name:-')
# salary=int(input('enter asalary:-'))    
# dispaly(name=name,salary=salary)  

print('#####################################################################')
#########################################################
# varaiable length argument
# def sum(*a):   #foramal argumernt#multiple value pass 
#     print(a)
#     for i in a:
#         for j in i:
#             print(j)
#         print(i)
# n=int(input('eneter a number of element you want to insert:-'))
# x=[]
# for i in range(n):
#     value=int(input('eneter a element:-'))        
#     x.append(value)
# sum(x)    


#HOW I CAN PASS MULTIPLE USER INPUET AS INTEGER TO THE FUNCTION.
#TYPES OF VARAIBLE
'''
LOCAL -THE VARAIABLE WHOSE SCOPE INSDE A FUNCTION  / inside function
GLOBAL-GLOBLA SCPOE /outsiode function
'''

x=2
def sum():
    y=3   #loacla varaible
    print(y)
    print(x)
sum()
# print(y)  #This willl throgh error because this is local varaiable we can not use local
 #varaiabkle ouside of function


 ############################################################################

 '''
 functioon
  #types of functiom

  1)built in  function
  2)user defined function
 
 #type of argument
 1) actual  argumnet
 2)formal argumnet

 #typed of actual argument
 1)positinal 
 2_keyword
 3)varaible lengh
 4)defaulrt
 5)keyword varaiable length

#types of varaiable 

 1)global var
 2) local var

 '''









