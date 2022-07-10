import requests
from bs4 import BeautifulSoup


url='https://www.codewithharry.com'

#getting the content

r=requests.get(url)

data=r.content

#print(data)

#parsing the content

soup=BeautifulSoup(data,'html.parser')
title=soup.title

#get all paratags. tags.
para_tags=soup.find_all('p')
#print(para_tags)

#get all anchor tags
ancor_tags=soup.find_all('a')

#to get elements with a particular class name
#print(soup.find('p')['class'])
#print(soup.find_all('p',class_="text-sm"))


#printing all anchor tag links.

all_links=set()

for link in ancor_tags:
    if link.get("href") !="#":
        all_links.add(url+link.get('href'))
        #print(all_links)



# getting all contents of a particular id
navs=soup.find(id="nav-content")

for ele in navs.stripped_strings:
    print(ele)


