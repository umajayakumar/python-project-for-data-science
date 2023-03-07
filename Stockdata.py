import yfinance as yf
import pandas as pd
import urllib
import urllib.request
import csv
import os
from xlsxwriter.workbook import Workbook
import logging
from bs4 import BeautifulSoup, NavigableString
import requests  # this module helps us to download a web page      
import time
import datetime as dt
from lxml import html
import xlsxwriter
import matplotlib.pyplot as plt
#import openpyxl
#import numpy as np


#script_dir = os.path.dirname(os.path.realpath(__file__))
#filename_excel = script_dir + "/output.xlsx"
#print(filename_excel)

GameStop=yf.Ticker("GME")
print(GameStop)
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'
html_data= requests.get(url)
#html_data=response.text
soup = BeautifulSoup(html_data.text, 'lxml')
all_tables=soup.find_all('table')
second_table=all_tables[1]
gme_revenue=second_table.find_all('tr')
print(gme_revenue)
gme_revenue= pd.DataFrame(columns=["Date","Revenue"])
for row in second_table.find_all('tr'):
    columns=row.find_all('td')
    if (columns != []):
        date = columns[0].text
        #if(date != 2021-6-1):
            #print("Upto june")
        revenue = columns[1].text
        gme_revenue = gme_revenue.append({"Date":date, "Revenue":revenue},ignore_index=True) 
        gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(',|\$',"")
        #gme_revenue.dropna(inplace=False)
        gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]
        
#print(gme_revenue)
final_list= gme_revenue.tail(3)
print(final_list)
for row in final_list:
    col1=final_list['Date'].to_string(index=False)
    col2=final_list['Revenue'].to_string(index=False)
print(col1)
print(col2)
# x=dt.date(2003, 6, 1)
# y=int['col2']
# plt.plot(x,y)

# plt.xlabel('Date')
# # naming the y axis
# plt.ylabel('Revenue')
  
# # giving a title to my graph
# plt.title('My first graph!')
# plt.show()






    



