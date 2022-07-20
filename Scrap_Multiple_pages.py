#import Libraries 
import requests

from bs4 import BeautifulSoup

import pandas as pd


list= []
headers = []

#loop through Several Pages
for page in range(1,100,1):
    
    page_url = "https://adoption.com/baby-names/origin/Egyptian?page=" + str(page)
     
    page_1 = requests.get(page_url)
    
    soup = BeautifulSoup(page_1.content,'html.parser')

    table  = soup.find('table', class_= 'table table-striped table-bordered')
    
    
    #find the table headers
    for i in table.find_all('th'):
        title = i.text
        headers.append(title)
    
    if len(headers) ==5:
        mydata = pd.DataFrame(columns = headers)
    
    

    temp = []


    #find the row data into table 
    for j in table.find_all('tbody'):
    
        row_data = j.find_all('td')

    for i in row_data:

        if len(i.text.strip()) >= 1:

            temp.append(i.text.strip())



        if len(temp) == 5:

            length = len(mydata)
            
            mydata.loc[length] = temp

            #mydata= temp
            
            #mydata.append(pd.Series(temp,index =mydata.columns[:len(mydata)]), ignore_index=False)

            temp = []

       
#save file as csv
origin = 'Egyptian'
 
mydata.to_csv(f'C:/Users/Harold.eshun/Downloads/Muslims/{origin}.csv',index=False)
