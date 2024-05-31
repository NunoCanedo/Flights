## Import Libraries



import time
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import csv
import pandas as pd

import undetected_chromedriver as uc


#driver = uc.Chrome()



options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('--disable-blink-features=AutomationControlled')

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)



#driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

date = datetime.date.today()
initial_date = '2024-06-13'
foo = '2024-09-30'

url = f'https://www.kayak.co.uk/flights/LGW-OPO/{initial_date}/{foo}?sort=bestflight_a'



## Function to accept cokkies

def click(selector):
       
    try:
        driver.find_element(By.XPATH, selector).click()
            
    except NoSuchElementException:
        return False
    


## Function to TRY and Extract the individual data from each product in the Page being scraped
        
def extract_data(product, selector):
  try:
    return product.select_one(selector).text
  except AttributeError:
    return None




## Specific function for the airline name
        
def airline_name(product, selector):
  try:
    return product.select_one(selector, alt=True)['alt']
  except TypeError:
    return None


##Function to extra data from flights

def flight_data(url):

    driver.get(url)
    time.sleep(3)

    click('/html/body/div[5]/div/div[2]/div/div/div[3]/div/div[1]/button[1]/div/div')

    time.sleep(10)
    soup=BeautifulSoup(driver.page_source,'lxml')
    data = soup.select('#listWrapper > div > div:nth-child(2) > div > div > div > div.nrc6-wrapper')

    for item in data:
        
        info = {
            'search_date': date,
            'outbound_flight_date': initial_date,
            'outbound_airline': airline_name(item, 'div > ol > li:nth-child(1) > div > div > div.tdCx-mod-spaced.tdCx-mod-stacked > div > div > div > img'),
            'outbound_departure_hour': extract_data(item, 'div > ol > li:nth-child(1) > div > div > div.VY2U > div.vmXl.vmXl-mod-variant-large > span:nth-child(1)'),
            'outboud_arrival_hour': extract_data(item, 'div > ol > li:nth-child(1) > div > div > div.VY2U > div.vmXl.vmXl-mod-variant-large > span:nth-child(3)'),
            'outbound_departure_airport': extract_data(item, 'div > ol > li:nth-child(1) > div > div > div.VY2U > div.c_cgF.c_cgF-mod-variant-full-airport > div > div:nth-child(1) > span > span:nth-child(1)'),
            'outbound_arrival_airport': extract_data(item, 'div > ol > li:nth-child(1) > div > div > div.VY2U > div.c_cgF.c_cgF-mod-variant-full-airport > div > div:nth-child(3) > span > span:nth-child(1)'),
            'outbound_flight_duration': extract_data(item, 'div > ol > li:nth-child(1) > div > div > div.xdW8.xdW8-mod-full-airport > div.vmXl.vmXl-mod-variant-default'),
            'outbound_flight_stops': extract_data(item, 'div > ol > li:nth-child(1) > div > div > div.JWEO > div.vmXl.vmXl-mod-variant-default > span'),
            
            'inbound_flight_date': foo,
            'inbound_airline': airline_name(item, 'div > ol > li:nth-child(2) > div > div > div.tdCx-mod-spaced.tdCx-mod-stacked > div > div > div > img'),
            'inbound_departure_hour': extract_data(item, 'div > ol > li:nth-child(2) > div > div > div.VY2U > div.vmXl.vmXl-mod-variant-large > span:nth-child(1)'),
            'inboud_arrival_hour': extract_data(item, 'div > ol > li:nth-child(2) > div > div > div.VY2U > div.vmXl.vmXl-mod-variant-large > span:nth-child(3)'),
            'inbound_departure_airport': extract_data(item, 'div > ol > li:nth-child(2) > div > div > div.VY2U > div.c_cgF.c_cgF-mod-variant-full-airport > div > div:nth-child(1) > span > span:nth-child(1)'),
            'inbound_arrival_airport': extract_data(item, 'div > ol > li:nth-child(2) > div > div > div.VY2U > div.c_cgF.c_cgF-mod-variant-full-airport > div > div:nth-child(3) > span > span:nth-child(1)'),
            'inbound_flight_duration': extract_data(item, 'div > ol > li:nth-child(2) > div > div > div.xdW8.xdW8-mod-full-airport > div.vmXl.vmXl-mod-variant-default'),
            'intbound_flight_stops': extract_data(item, 'div > ol > li:nth-child(2) > div > div > div.JWEO > div.vmXl.vmXl-mod-variant-default > span'),
            
            
            'price': item.select_one('div.f8F1-price-text').text   
            }
        flights = []
        flights.append(info)
        df = pd.DataFrame(flights)
        df.to_csv('flights_date.csv', index = False)
        
        
        
        

if __name__ == '__main__':
  flight_data(url)