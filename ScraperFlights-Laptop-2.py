import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from datetime import datetime


url = 'https://www.kayak.co.uk/flights/LGW-OPO/2024-05-24/2024-05-30?sort=bestflight_a'

session = HTMLSession()

response = session.get(url)
#response.html.render()

#print(response.html)
#print(response.html.find('div.f8F1-price-text'))





start_date = '05-3-2024'
date_object = datetime.strptime(start_date, '%m-%d-%Y').date()

print(date_object)
print(type(date_object))
min_days = 4
max_days = 12

#last_day = date_object + datetime.timedelta(days=min_days)
#print(last_day)
end_date = '2024-06-30'

