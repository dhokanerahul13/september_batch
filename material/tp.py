#generator-generator are used to generate sequence of value ONE BY ONE
#YIELD- IT WIL CREATE GENERATOR FUNCTION


#iterator- for loop work on iter protocol so for looop have-iter and next method\

#iter()-IT WILL CREATE ITERATOR OBJECT
#NEXT()-IT WILL PRINT NEXT VALUE FROM ITERATOR OBJECT.

def add(): 
    yield 1
    yield 2
    yield 3
print(add())           
x=add()
print(next(x))
print(next(x))
print(next(x))


print('#####################################################')
l=[1,2,34]
x=iter( l)  #iterator object
print(next(x))  #traversing memeber of iterator object one by one
print(next(x)) 
print('this is ABOUT GENERATOR')
def add(B): 

    for i in B:
        return i
  

l=[1,2,3,4]    
print(add(l)) 
print(add(l)) 
# print(next(add(l)))       
# print(next(add(l)))    


def hello(list1):
    for i in list1:
        return i
list1=[1,2,233,44,44] 
print(hello(list1))       
#################################################################
#go through this

'''
iter()
iterator
generator
return
yield
next()
chaing of decorator
add decoartor manually

'''