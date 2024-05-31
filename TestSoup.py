import asyncio
from arsenic import get_session, browsers, services


import time
import datetime
import csv
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
from datetime import date





#url = f'https://www.kayak.co.uk/flights/LGW-OPO/{departure_date}/{arrival_date}?sort=bestflight_a'

date = date.today()

first_day = '06-29-2024'
first = datetime.strptime(first_day, '%m-%d-%Y').date()
    
    
last_day = '09-30-2024'
last = datetime.strptime(last_day, '%m-%d-%Y').date()

minimum_days = 4

maximum_days = 12

duration_days = range(4, 12)

## Function to extract the price


def extract_price(product, selector):
    
    try:
        return product.select_one(selector).text
    except AttributeError:
        return None
    
    



## Function to extract data 

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


async def save_data(info):
    
    
    flights = []
    
    flights.append(info)
            
            
    #df = pd.DataFrame(flights)   
    
    #df.to_csv('flights_data2.csv', index = False)   
            
    df = pd.read_csv('flights_data2.csv')
            
    for x in flights:
        df = df._append(x, ignore_index = True)
            
        df.to_csv('flights_data2.csv', index = False)
    
    


async def flights_data(body, departure_date, arrival_date):
    
    
    soup = BeautifulSoup(body, 'lxml')
            
    data = soup.select('#listWrapper > div > div:nth-child(2) > div > div > div > div.nrc6-wrapper')
    
    for item in data:
            
            info = {
                'search_date': date,
                'outbound_flight_date': departure_date,
                'outbound_airline': airline_name(item, 'div > ol > li:nth-child(1) > div > div > div.tdCx-mod-spaced.tdCx-mod-stacked > div > div > div > img'),
                'outbound_departure_hour': extract_data(item, 'div > ol > li:nth-child(1) > div > div > div.VY2U > div.vmXl.vmXl-mod-variant-large > span:nth-child(1)'),
                'outboud_arrival_hour': extract_data(item, 'div > ol > li:nth-child(1) > div > div > div.VY2U > div.vmXl.vmXl-mod-variant-large > span:nth-child(3)'),
                'outbound_departure_airport': extract_data(item, 'div > ol > li:nth-child(1) > div > div > div.VY2U > div.c_cgF.c_cgF-mod-variant-full-airport > div > div:nth-child(1) > span > span:nth-child(1)'),
                'outbound_arrival_airport': extract_data(item, 'div > ol > li:nth-child(1) > div > div > div.VY2U > div.c_cgF.c_cgF-mod-variant-full-airport > div > div:nth-child(3) > span > span:nth-child(1)'),
                'outbound_flight_duration': extract_data(item, 'div > ol > li:nth-child(1) > div > div > div.xdW8.xdW8-mod-full-airport > div.vmXl.vmXl-mod-variant-default'),
                'outbound_flight_stops': extract_data(item, 'div > ol > li:nth-child(1) > div > div > div.JWEO > div.vmXl.vmXl-mod-variant-default > span'),
                
                'inbound_flight_date': arrival_date,
                'inbound_airline': airline_name(item, 'div > ol > li:nth-child(2) > div > div > div.tdCx-mod-spaced.tdCx-mod-stacked > div > div > div > img'),
                'inbound_departure_hour': extract_data(item, 'div > ol > li:nth-child(2) > div > div > div.VY2U > div.vmXl.vmXl-mod-variant-large > span:nth-child(1)'),
                'inboud_arrival_hour': extract_data(item, 'div > ol > li:nth-child(2) > div > div > div.VY2U > div.vmXl.vmXl-mod-variant-large > span:nth-child(3)'),
                'inbound_departure_airport': extract_data(item, 'div > ol > li:nth-child(2) > div > div > div.VY2U > div.c_cgF.c_cgF-mod-variant-full-airport > div > div:nth-child(1) > span > span:nth-child(1)'),
                'inbound_arrival_airport': extract_data(item, 'div > ol > li:nth-child(2) > div > div > div.VY2U > div.c_cgF.c_cgF-mod-variant-full-airport > div > div:nth-child(3) > span > span:nth-child(1)'),
                'inbound_flight_duration': extract_data(item, 'div > ol > li:nth-child(2) > div > div > div.xdW8.xdW8-mod-full-airport > div.vmXl.vmXl-mod-variant-default'),
                'intbound_flight_stops': extract_data(item, 'div > ol > li:nth-child(2) > div > div > div.JWEO > div.vmXl.vmXl-mod-variant-default > span'),
                
                
                'price': extract_data(item, 'div.f8F1-price-text')  
                }
            #return info
        
            await save_data(info)
    
    
    
    
    



async def scraper(limit, departure_date, arrival_date):
    
    
    
    service = services.Chromedriver(binary = r"C:\Users\nuno_\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe")
    browser = browsers.Chrome()
    browser.capabilities = {
        'goog:chromeOptions': {"args": ['--disable-gpu', '--no-sandbox', '--disable-dev-shm-usage']}    
        }
    
    async with limit:
        async with get_session(service, browser) as session:
    
            await session.get(f'https://www.kayak.co.uk/flights/LGW-OPO/{departure_date}/{arrival_date}?sort=bestflight_a')

            body = await session.get_page_source()
            
            await flights_data(body, departure_date, arrival_date)
            






async def first_last_day():
    
    limit = asyncio.Semaphore(10)
    
    import datetime
    
    a = 0
    
    departure_date = first
    
    while departure_date < last - datetime.timedelta(days=4):
        
        departure_date = first + datetime.timedelta(days=a)
        
        time.sleep(60) 
    
    
    
    
        for x in duration_days:
            
            
            #departure_date = first
            
            arrival_date = departure_date + datetime.timedelta(days=x)
                        
            
            
            if arrival_date <= last:
                await scraper(limit, departure_date, arrival_date)
                
            else:
                break
            
        a+=1
                
            
    
    
    
    
    
if __name__ == '__main__':
    start = time.time()
    asyncio.run(first_last_day())
    end = time.time()
    print(f'total time is: {end}')