'''

def functionname(arguments):
    statmenrts about functions
'''

#decorator
'''

decorator is function whicha can take a function as a argument and add some functinality
and return it without modifing existing function..cls

'''
#1)various names can be bound to the same function object.

def admin():
    return 'hi i am admin'
x=admin()    # here x is function object/ variable
y=x  #function object addign
print(y)
del x
print('#########################################')
print(y)

########################################################################

#2)function can be passed as argument to another function
#such function that take other functionas argument are also called higher order function.
print('############################################################')
def increment(x):#THE FUNCTION WHICH PASSEDCT TO A FUNCTION AS ARGUMENT
    print('increment of ',x,"=",x+1)
def decrement(x):
    print('decrement of ',x,"=",x-1)
def calculate(func,x):#existing function
    return func(x)
calculate(increment,10)     
calculate(decrement,6)       
#######################################################################
print('#################################################')
def lower_case(txt):
    return txt.lower()
x=lower_case('taskdfhj')    
def upper_case(txt):
    return txt.upper()
def format_text(x):
    text=x('Hello everyone this is basic function')
    print(text)       
format_text(lower_case)
format_text(upper_case)
##########################################################################################
#3)a function can return another function
print('##################################################################')
def calculation():
    def addition(x,y):
        print('addition os ',x, 'and ',y,'=',x+y)
    return addition
add =calculation()
add(5,6)    
    
'''
when to use decorator
#you will use decorator when you need to change the behavior of a function
without modifing funtion itself.
#you can also use one when you need to run same code on multiple functyion.
#this can avboid writing duplicate functiom.
#codeb reusabilioty.


syntax:-

def mydeco(func):
    def inner_func():
        do something change
    return inner_func    

'''    
print('####################################################')
def upper_case(func):  #decorator function
    def inner_func(txt):
        func(txt.upper())
    return inner_func

@upper_case
def priint_txt(txt):  #main function where you can perform changes
    print(txt)
priint_txt('hello')     


###########################################################################
#example number two
print('############################################################')
#with @decorator
def smart_div(func): #decoratove function
    def inner(a,b):
        print('i am divideing',a,'and ','b')
        if b==0:
            print('we can not devide by 0')
        else:
            func(a,b)
    return inner

@smart_div
def division(a,b): #maIN FUNCTION
    print('division',a/b)
division(4,0)    

#############################################################
#without using @ decorator
# def smart_div(func): #decoratove function
#     def inner(a,b):
#         print('i am divideing',a,'and ','b')
#         if b==0:
#             print('we can not devide by 0')
#         else:
#             func(a,b)
#     return inner
# def division(a,b): #maIN FUNCTION
#     print('division',a/b)

# y=smart_div(division(1,1))
# print('#########')
# y()


###########################################################

def decor(num):
    def inner():
        a=num()
        multi=a*5
        return multi
    return inner
def num():
    return 10
x=decor(num)           
print(x())

####################################################################

#we will discuss tomorrow
print('####################################################')

# def hello_decorator(func):
#     def inner(x,y):
#         print('before execution of decorator')
#         return_value=func(x,y)
#         print('after execution')
#         return return_value
#     return inner    

# def sum_of_number(a,b):
#     return a+b        
# # print(sum_of_number(1,2))    

# y=hello_decorator(sum_of_number(3,2))
# print(y())



#decorator chaining

def sqrt(func):
    def inner():
        x=func()
        return x*x
    return inner
def decor(func):
    def inner():
        x=func()
        return 2*x
    return inner   
@sqrt
@decor
def num():
    return 3
print(num())    

#################################################

print('##########################################################')
def decor1(func):
    def inner():
        x=func()
        multi=x*5
        return multi
    return inner
def decor(func):
    def inner():
        x=func()
        add=x+5
        return add
    return inner   
@decor1    
@decor
def num():
    return 3
print(num())  
num=decor(decor1(num))
print(num())


####################################################################
#how tob pass argumnt manually in decorator????example???
