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



