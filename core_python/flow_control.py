#flow control describe the order in which statement will be executed.

'''
1)conditinal statement-to specify perticular condition
if
if-else
if-elif-else

2)tranfer statemet-

break
continue
 pass

3)iterative-
for loop
 while loop
'''
#1)if
'''
if condition:
    statement
    statment
if condition is true then statemnr5 will execute    

#indentation-indentation refer to four spaces that is used for executing statment for a pertiular blocjk
'''
#if-else
'''
if condition:
    actin-1
else: 
    action-2
if condition is true then action-1 wil be executed otherise action 2 will be executeed        
'''
num=int(input('enter a nuber:-'))
if num>20:
    print('number is greater tahn 20')
else:
    print('number is not greater than 20')    

#if-elif-else-to use multi way condition
'''
if conidtion1:
    action-1
elif  condition2:
    action2
elif codition3:
    acition 3
else:
    default action        
'''    

day=input('enter a day:-')
if day=='monday':
    print('today is monday')
elif day=='tuesday':
    print('today id tuesday')
elif day=='wednesday':
    print('today is wednesday')
elif day=='friday':
    print('today is friday')
else:
    print('today is holiday')              
# 
# 
#iterative statements
'''
 if we want to execute group of statment mulyiple timesthen we shoud go for iterative  statement.
1) for looop
if we wanrt to execute some action for every element present in some sequence


sequence-string,list,tuple,dict
#syntax

for element in sequence:
    element
'''  
from unicodedata import name


s='today is good day to learn python'
#len(s)- number of times  loop will run
for char in s:
    print(char)
print('########################################################')
#without indesx 
list1=[1,2,3,4,5,5]
for element in list1:
    print(element)    

#print element and index of element of sequence.
print('##############################################')
s='happy'
for i in range(len(s)):
    print('index is:_',i,'charecter of string',s[i])
print('##########################################################')
list1=[1,2,3,4,5]
for i in range(len(list1)):
    print('index of list1:-',i,'element of list:-',list1[i])
print('###############################################################')


list1=[1,2,3,34,4,5]

# print(len(list1))
#without index
for var in list1:  #len(list1),1,2,3,43,4,5
    print(var,list1)  #element form 0-end

#with index
for var in range(len(list1)):
    print('index of list1:-',var,'element of list:-',list1[var]) 
####################################################################
print('#######################################################')
#program to print even number from a list
list=[1,2,3,34,4,5,5,4,6,76] 

for i in range(len(list)):
    if list[i]%2==0:
        print('index of even number is',i,'element is ',list[i])

#generate number for arange function using a for loop

for i in range(100):
    print(i) 

#sum of element present in a list
list1=[1,2,2,3,4]
sum=0
for i in range(len(list1)):
    sum=sum+list1[i]
print(sum)   

print('##############################################')
#reverse list1 without index
for i in list1[::-1]:
    print(i)

print("###################################################")
#reverse list1 with index  #inbuilt method of ,list
# for i in range(len(list1)):
#     print(i)    

#while loop
'''
if we want to execute a group os statement until some condition false then we should go for 
while loop


syntac

while condition:
    body

'''
i=6  #start condition
while i<15:  #condition where loop will termianate
    print(i)
    i+=1 # this will increment your start condition  to achive base condition 

#conditinal statemnte
'''
 if
  if-else
   if-elif,else

'''
#iterative
'''
for loop 
while loop
'''    
############################################################
#transfer statement
#1)break-thisa will terminate the looop when condition satofied
for i in range(10):
    print(i)


print('#####################################################')
i=0    #start
while i>10000:  #conndidtion
    print(i)  #print(i)