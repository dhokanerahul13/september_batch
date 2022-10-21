#transfer statement
#1)break-thisa will terminate the looop when condition satofied
# for i in range(10):
#     if i==6:
#         break
#     print(i)


print('#######################################################')
# list1=[1,2,2,3,4,4,5,6,7]
# for i in list1:
#     if i==5:
#         break
#     print(i)
#continue-continue used to skip current interations
print('######################################')
# for i in range(10):
#     if i==5:
#         continue
#     print(i)  


#pass- do nothing passs the iteration

'''
in programmingh if block requied which wont do anything then we
 can defne that block with pass keyword
'''
print('###############################################################')
# for i in range(10):
#     if i==5:
#         pass
#     print(i)



print('#####################################################')
i=0    #start
while i<=10000:  #conndidtion
    # print(i)  #print(i)    
    if i%2==0:
        continue
    print(i)
    i+=1