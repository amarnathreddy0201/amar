from selenium import webdriver
from  bs4 import BeautifulSoup
import pandas as pd
import csv
import requests

#driver = webdriver.Chrome("../python_selenium/chromedriver")

#this is for  getting the link of the data
url="https://www.bikewale.com/royalenfield-bikes/"
page=requests.get(url)


soup=BeautifulSoup(page.content,'html.parser')

#print(soup.text)
#images

img_list=[]
image=soup.findAll('div',class_="imageWrapper")
#print(image)
for i in image:
    j=i.img['src']
    #print(j)
    img_list.append(j)

#print(img_list)




links_list=[]
links=soup.findAll('div',class_="bikeDescWrapper")
for i in links:
    links_list.append(i.a['href'])

#print(links_list)



#text
text_list=[]
text=soup.findAll('div',class_="bikeDescWrapper")
for i in text:
    #print(i.a.text)
    text_list.append(i.a.text)
#print(text_list)

#This is the entir data comined into dictionary
extract_data={"images":img_list,"link":links_list,"text":text_list}

#Dataframe for getting values row and colum vise 
#panda=pd.DataFrame(extract_data)
#print(panda)
#panda.to_csv("webscrap_bullet.csv")




#using csv store the all data
#This is wrong '''I am gona change this'''
img1=0
with open("il.csv","w") as csv_file:
    write=csv.writer(csv_file)
    write.writerow(csv_file)
    for i in image:
        j=i.img['src']
        img1.append(j)
    write.writerow(img1)
    print(write)
