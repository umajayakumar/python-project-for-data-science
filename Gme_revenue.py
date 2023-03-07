import yfinance as yf
import pandas as pd
from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page
from lxml import html

  
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
        revenue = columns[1].text
        gme_revenue = gme_revenue.append({"Date":date, "Revenue":revenue}, ignore_index=True)
gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(',|\$',"")
gme_revenue.dropna(inplace=True)
gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]
print(gme_revenue.tail(5))
