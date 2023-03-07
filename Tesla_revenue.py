import yfinance as yf
import pandas as pd
from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page
from lxml import html

url = ' https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm'
r = requests.get(url)

#html_data=response.text
tesla = yf.Ticker("TSLA")
print(tesla)
tesla_data = tesla.history(period="max")
print(tesla_data)
soup = BeautifulSoup(r.text, 'lxml')
all_tables=soup.find_all('table')
second_table=all_tables[1]
tesla_revenue=second_table.find_all('tr')
#print(tesla_quaterly_revenue)
#tqr=tesla_quaterly_revenue
tesla_revenue= pd.DataFrame(columns=["Date","Revenue"])
for row in second_table.find_all('tr'):
#print(tqr.head(5))
    columns=row.find_all('td')
    if (columns != []):
        date = columns[0].text
        revenue = columns[1].text
        tesla_revenue = tesla_revenue.append({"Date":date, "Revenue":revenue}, ignore_index=True)
tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"")
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
print(tesla_revenue.tail(5))
