'''
collection of charecter inside single quote or double quote .
immutable
indexing/ slcing pssible
item assignment possible
insertion order preseeved
'''
#string folllow positive as well  as negetive indesing

s='today is good day to learn python'
print(s[0])
print(s[-1])

#slice
print(s[0:40:1])

#item assignment  
# s[1]=9   #str' object does not support item assignment
# print(s)


#LENRTH OF STRING USING LEN()   
print(len(s))



#concatinaton -" + " /conacatination-we can not concate string with number
# s='hello'
# r='raj'
# a=9
# print(s+' '+r+a)


#repeation operator string-*=we can not repeat the char with both strng atlest we want in number.


s=' hello'
r='raj'
a=9
print(s* a)


#membership opeartor
s='today is bad day'
print('good' in s)

#STRING IN BUILT METHODS
#1)INDEX()-THROGH INDEX OF PERTICULAR STRING
# S=input('enter a string:-')
# print(S.index('GOOD'))

#2)COUNT()- COUNT THE NUMBER OF OCCUURANCE OF STRING
# S=input('enter a string:-')
# print(S.count('a'))

#replace()-repalce the existing string with new one
s='today is good day'
s1=s.replace('good','bad')
print(id(s))
print(id(s1))

#split()-we can split the str according to your condition-string convert into list
s='amol hello how are you'
print(s.split('e'))
for i in s.split():
    print(i)


#changing case of string
'''
upper()
lower()
swapcase()
titlecase()
capitlize()

'''
print('#####################################################')
s='learning pythomn is very easy'
print(s.lower())
print(s.upper())
print(s.title())
print(s.capitalize())
print(s.swapcase())

##########################################################################
#foramating- variable and string attache to represent output
name='rahul'
age=28
salary=80000
#my name is rahul and my age is 28 now and i got 80000 salary
#noraml forammating
print('my name is',name,'and my age is',age,'and i got',salary)
#f string-{}-placeholder
print(f'my name is {name} and my age is {age} and i got {salary}')
#.foramt method
print('my name is {0} and my age is {1} and i got  {2}'.format(name,age,salary))
################################################################################
s='hello how are you'
for i in s:
    print(i)  # charecter
for i in range(len(s)):
    print('index is',i,'charedcter are:-',s[i])    
#########################################################################
i=0 
while i<1000:
    i+=1
    if i%2==0:
        continue
    print(i)