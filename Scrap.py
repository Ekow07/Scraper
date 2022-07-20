from lib2to3.pgen2.pgen import DFAState
from openpyxl import load_workbook
import requests

from bs4 import BeautifulSoup

import pandas as pd




url = "https://adoption.com/baby-names/origin/Arabic?page=16"

page_number = "?page="

page = requests.get(url)



soup = BeautifulSoup(page.content,'html.parser')

table  = soup.find('table', class_= 'table table-striped table-bordered')




headers = []



for i in table.find_all('th'):
    title = i.text

    headers.append(title)



 

mydata = pd.DataFrame(columns = headers)

temp = []



for j in table.find_all('tbody'):

    row_data = j.find_all('td')

    for i in row_data:

        if len(i.text.strip()) >= 1:

            temp.append(i.text.strip())



        if len(temp) == 5:

            length = len(mydata)

            mydata.loc[length] = temp

            temp = []



origin = 'Muslim_16'



mydata.to_csv(f'C:/Users/Harold.eshun/Downloads/Muslims/{origin}.csv',index=False)

''' FilePath = "C:/Users/Harold.eshun/Downloads/Muslims/Muslim_Reload.xlsx"
ExcelWorkbook = load_workbook(FilePath)
writer = pd.ExcelWriter(FilePath, engine = 'openpyxl')
writer.book = ExcelWorkbook
pd.DataFrame.to_excel(writer, sheet_name = 'Muslim_15')
writer.save()
writer.close()
 '''