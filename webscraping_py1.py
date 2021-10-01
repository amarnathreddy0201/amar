"""
webscraping about harddiscs
"""
from bs4 import BeautifulSoup as soup
import requests
import pandas as pd

try:

    myurl="https://www.newegg.com/global/in-en/p/pl?d=graphic+cards"

    page_html=requests.get(myurl)
    
    #html parser
    page_soup=soup(page_html.content,"html.parser")
    #print(page_soup.h1)
    #print(page_soup)

    #images
    images=page_soup.findAll('div',class_="item-container")
    

    title_list=[]
    images_list=[]
    price_list=[]
    #brand_list=[]
    #print(images)
    for i in images:
        
        #below 3 lines for collecting money
        j=i.find('li',attrs={'class':"price-current"})
        J=str(j)
        price_list.append(J[J.find("₹"):J.find("<!")])
        
        images_list.append(i.a.img['src'])#image list    
        title_list.append(i.a.img["title"])#title list
        
       
        

    #print(images_list)
    #print(title_list)
    #print(price_list)
    #create the dictionary using images titles and prices
    egg={"image_list":images_list,"title_list":title_list,"price_list":price_list}
    panda=pd.DataFrame(egg)
    print(panda)
    panda.to_csv("newegg.csv")

    
    

except Exception as e:
    print("except",e.__cause__)

else:
    print("thank god don have any error")

finally:
    print("finally i completed")
