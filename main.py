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
import random
#import undetected_chromedriver as uc


#proxy = '66.191.31.15' ## Testing with Proxies
options = webdriver.ChromeOptions()
#options.add_argument('--headless=new')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--ignore-certificate-errors')
options.add_argument("--disable-extensions")
#options.add_argument(f"--proxy-server={proxy}") ## Testing with Proxies
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument('--allow-running-insecure-content')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36')


options.add_argument("start-maximized")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

#ptions = uc.ChromeOptions()
#options.headless = True
#options.add_argument( '--headless=new' )
#driver = uc.Chrome()


date = datetime.date.today()

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

def flight_data(url, initial_date, foo):

    driver.get(url)
    print(url)
    time.sleep(3)

    click('/html/body/div[5]/div/div[2]/div/div/div[3]/div/div[1]/button[1]/div/div')
    
    limit = random.randint(10, 20)
    
    time.sleep(10)
    soup=BeautifulSoup(driver.page_source,'lxml')
    data = soup.select('#listWrapper > div > div:nth-child(2) > div > div > div > div.nrc6-wrapper')

    flights = []
    
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
        
        flights.append(info)
        print(info)
        
        
        
        
        
        df = pd.read_csv('flights_data.csv')
        
    for x in flights:
        df = df._append(x, ignore_index = True)
        
        df.to_csv('flights_data.csv', index = False)




def url():
    
    ## first_day >> start_date() << will be a function
    ## last_day >> end_date() << will be a function
    ## lenght >> duration() <<  will be a function
    
    from datetime import datetime
    first_day = '07-03-2024'
    date_first = datetime.strptime(first_day, '%m-%d-%Y').date()
    #print(type(date_first))
    #print(date_first)
        
    last_day = '09-30-2024'
    date_last = datetime.strptime(last_day, '%m-%d-%Y').date()
    #print(type(date_last))
    #print(date_last)
    
    
    import datetime 
    interval = range(4, 12)
    
    a = 0
    initial_date = date_first + datetime.timedelta(days=a)
    

    
    while initial_date < date_last:
        
        
        initial_date = date_first + datetime.timedelta(days=a)
        final_date = date_last
        
        
        url = f'https://www.kayak.co.uk/flights/LGW-OPO/{initial_date}/{final_date}?sort=bestflight_a'
        #print(initial_date, '             ', final_date)
        print(url)
        #limit = random.randint(1, 120)
        #time.sleep(limit) 
        for x in interval:
            
            foo = initial_date + datetime.timedelta(days=x)
            final_url = f'https://www.kayak.co.uk/flights/LGW-OPO/{initial_date}/{foo}?sort=bestflight_a'
            
            if foo <= date_last:
                flight_data(final_url, initial_date, foo)
                
            else:
                break
        
        a+=1
    

 
    
    
    
url()