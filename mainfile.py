from bs4 import BeautifulSoup 
import requests 
from openpyxl.reader.excel import load_workbook



#Создание книги Excel



def parse():
    
    doc = load_workbook(filename='goo.xlsx')
    ws = doc.active #Создание книги Excel и рабочего листа


    url = 'https://www.chitai-gorod.ru/' #Запрос на сайт
    page = requests.get(url) 
    print(page.status_code)
    soup = BeautifulSoup(page.text, "html.parser") 


    allAuthors = soup.findAll('div', class_='product-title__author') 
    allNames = soup.findAll('div', class_='product-title__head' )
    allPrices = soup.findAll('div', class_='product-price__value')
    def sortExcel(): #Функция заполнения ячеек Excel
        i = 1
        j = 1
        for auth in allAuthors:
            if auth is not None:
                ws.cell(row=j, column =i).value = auth.text        
                j += 1
        i += 1
        j = 1
        for name in allNames:
            ws.cell(row=j, column = i).value = name.text
            j += 1
        i += 1
        j = 1
        for price in allPrices:
            ws.cell(row=j, column = i).value = price.text
            j += 1 

        doc.save('goo.xlsx')

    sortExcel()
parse()





