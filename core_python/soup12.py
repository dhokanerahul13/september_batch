from bs4 import BeautifulSoup

import requests
# Giving url
url = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"
# Reading all content
content1 = requests.get(url)
# Passing the content to function
soup = BeautifulSoup(content1.content, 'html.parser')
# print(soup)
# print('_________________________________________________________________________')
# Printing content
# print('\nAll contents of Websites')
# print(soup.prettify())
# x=soup.prettify()
# Printing title of website
# print('_________________________________________________________________________')
print(soup.find('title.'))
print(soup.title.text)
# print('__________________
for link in soup.find_all('td'):
    pass
table1=soup.find('table',class_='chart full-width')
td1=table1.find_all('a')
list1=[]
list2=[]
for i in td1:
    if i.text=='\n':
        continue
    else:
        list1.append(i.text)
for j in table1.find_all('strong'):
    list2.append(j.text)
# print(list1) 
# for i in list1:
#     print(list1[i])
    # if list1[i]%2==0:
        # print(i)
# list1.remove('\n')
# print(list2)
c=list1.count(' \n')
for n in range(c):
    list1.remove(' \n')
print(list1)
print(list2)
d=dict(zip(list1,list2))
# print(d)
for i,j in d.items():
    print(i,j)