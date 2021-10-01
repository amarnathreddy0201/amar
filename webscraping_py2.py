

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

try:

    driver = webdriver.Chrome(ChromeDriverManager().install())

    products=[] #List to store name of the product
    prices=[] #List to store price of the product
    ratings=[] #List to store rating of the product
    driver.get("https://www.flipkart.com/laptops/a~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp;amp;amp;amp;uniq")

    content = driver.page_source


    soup = BeautifulSoup(content,'html.parser')


    for a in soup.findAll('div', attrs={'class':'_2kHMtA'}):
        
        
        #product name 
        name=a.find('div', attrs={'class':'_4rR01T'})
        name1=str(name)
        res=name1[name1.find(">")+1:name1.find("</")]
        if res=="Non" or res=="None":
            products.append("None")
            continue
        print("product name",res)
        products.append(res)
        
        

        
        #prices of products
        price=a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
        J=str(price)
        res=J[J.find("₹"):J.find("</")]
        print("price of products",res)
        if res=="Non" or res=="None":
            prices.append("None")
            continue
        print(res)
        prices.append(res)
        
        
        
        
        
        
        #rating of products
        rating=a.find('div', attrs={'class':'_3LWZlK'})
        J=str(rating)
        rate=J[(J.find(">"))+1:J.find("<i")]
        print("rating of products:",rate)
        if rate=="None" or rate=='Non':
            prices.append("None")
            continue
        #print(rate)
         
        prices.append(rate)
        
       
        
        
      

    df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
    df.dropna(axis='columns',inplace=True,how='all')
    print(df)
    df.to_csv('products.csv')
    print("data is store in products.csv")
    

except Exception as e:
    print(e)

finally:
    driver.quit()
    print("finally")



