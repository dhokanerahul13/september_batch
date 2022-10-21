
#program to prnt biggest of two
def biggestftwo(a,b):
    if a>b:
        print('a is greater than b')
    else:
        print('b is greater than a')    
n=int(input('enter a first num:-'))
n1=int(input('enter a seconfd num:-'))
biggestftwo(n,n1)
#biggest of three number
def biggestftwo(a,b,c):
    if a>b and a>c:
        print('a is greater than  b and c')
    elif b>c:
        print('b is greater than a nad c')
    else:
        print('c is greater tahn a and b ')    
n1=int(input('enter a first num:-'))
n2=int(input('enter a seconfd num:-'))
n3=int(input('enter a third num:-'))
biggestftwo(n1,n2,n3)

#largest num from list
def largestnum(a):
    print(a)
    print(max(a))  # with the help of inbilt funtion
    a.sort()
    print(a)
    print('largest num from a list id:-',a[-1])
n=int(input('eneter a number of element you want to insert:-'))
x=[]
for i in range(n):
    value=int(input('eneter a element:-'))        
    x.append(value)
largestnum(x)
#string-if string is immuatbal e then how we can chn age the content by using reaplace()

s='today is good dAY'
y=s.replace('t','r')
#directly object change
print(id(s))
print(id(y))
#program to print reverse order of word.  #try this with the help of function
s='today is good dAY'
y=s.split()
print(y)
print(y[::-1])
reverse=[]
for i in y[::-1]:
    reverse.append(i)
print('reverse word list is:-',reverse)    
#program to  revere internal content of each word
s='yadoy si doog yad'   #expected output
s=input('eneter a string:-')
l=s.split()
l1=[]
for i in range(len(l)):
    l1.append(l[i][::-1])
print(l1)
#remove duplicate charecter from a strng
n=input('enetr a string:-')
l=[]
for i in n:
    if i not in l:
        l.append(i)
print(l)      
#string without duplicate
z=''.join(l)
print(z)  