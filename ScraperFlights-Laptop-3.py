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




driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

date = datetime.date.today()
initial_date = '2024-05-27'
foo = '2024-05-30'

url = f'https://www.kayak.co.uk/flights/LGW-OPO/{initial_date}/{foo}?sort=bestflight_a'



## Function to accept cokkies

def click(selector):
       
    try:
        driver.find_element(By.XPATH, selector).click()
            
    except NoSuchElementException:
        return False
    
    

driver.get(url)
time.sleep(3)

click('/html/body/div[6]/div/div[2]/div/div/div[3]/div/div[1]/button[1]/div/div')
time.sleep(10)
soup=BeautifulSoup(driver.page_source,'lxml')
data = soup.select('#listWrapper > div > div:nth-child(2) > div > div > div > div.nrc6-wrapper')

for item in data:
    from datetime import datetime
    info = {
        'search_date': date,
        'outbound_flight_date': initial_date,
        'outbound_airline': item.select_one('div > ol > li:nth-child(1) > div > div > div.tdCx-mod-spaced.tdCx-mod-stacked > div > div > div > img', alt=True)['alt'],
        'outbound_departure_hour': item.select_one('div > ol > li:nth-child(1) > div > div > div.VY2U > div.vmXl.vmXl-mod-variant-large > span:nth-child(1)').text,
        'outboud_arrival_hour': item.select_one('div > ol > li:nth-child(1) > div > div > div.VY2U > div.vmXl.vmXl-mod-variant-large > span:nth-child(1)').text,
        'outbound_departure_airport': item.select_one('div > ol > li:nth-child(1) > div > div > div.VY2U > div.c_cgF.c_cgF-mod-variant-full-airport > div > div:nth-child(1) > span > span:nth-child(1)').text,
        'outbound_arrival_airport': item.select_one('div > ol > li:nth-child(1) > div > div > div.VY2U > div.c_cgF.c_cgF-mod-variant-full-airport > div > div:nth-child(3) > span > span:nth-child(1)').text,
        'outbound_flight_duration': item.select_one('div > ol > li:nth-child(1) > div > div > div.xdW8.xdW8-mod-full-airport > div.vmXl.vmXl-mod-variant-default').text,
        'outbound_flight_stops': item.select_one('div > ol > li:nth-child(1) > div > div > div.JWEO > div.vmXl.vmXl-mod-variant-default > span').text,
        
        'inbound_flight_date': foo,
        'inbound_airline': item.select_one('div > ol > li:nth-child(2) > div > div > div.tdCx-mod-spaced.tdCx-mod-stacked > div > div > div > img', alt=True)['alt'],
        'inbound_departure_hour': item.select_one('div > ol > li:nth-child(2) > div > div > div.VY2U > div.vmXl.vmXl-mod-variant-large > span:nth-child(1)').text,
        'inboud_arrival_hour': item.select_one('div > ol > li:nth-child(2) > div > div > div.VY2U > div.vmXl.vmXl-mod-variant-large > span:nth-child(1)').text,
        'inbound_departure_airport': item.select_one('div > ol > li:nth-child(2) > div > div > div.VY2U > div.c_cgF.c_cgF-mod-variant-full-airport > div > div:nth-child(1) > span > span:nth-child(1)').text,
        'inbound_arrival_airport': item.select_one('div > ol > li:nth-child(2) > div > div > div.VY2U > div.c_cgF.c_cgF-mod-variant-full-airport > div > div:nth-child(3) > span > span:nth-child(1)').text,
        'inbound_flight_duration': item.select_one('div > ol > li:nth-child(2) > div > div > div.xdW8.xdW8-mod-full-airport > div.vmXl.vmXl-mod-variant-default').text,
        'inbound_flight_stops': item.select_one('div > ol > li:nth-child(2) > div > div > div.JWEO > div.vmXl.vmXl-mod-variant-default > span').text,
        
        
        'price': item.select_one('div.f8F1-price-text').text   
        }
    print(info)


##listWrapper > div > div:nth-child(2) > div > div:nth-child(4) > div.yuAt.yuAt-pres-rounded > div > div > div.nrc6-content-section > div.nrc6-main > div > ol > li:nth-child(2) > div > div > div.tdCx-mod-spaced.tdCx-mod-stacked > div > div > div > img
##listWrapper > div > div:nth-child(2) > div > div:nth-child(1) > div > div.nrc6-wrapper > div > div.nrc6-content-section > div.nrc6-main > div > ol > li:nth-child(1) > div > div > div.tdCx-mod-spaced.tdCx-mod-stacked > div > div > div > img
##listWrapper > div > div:nth-child(2) > div > div:nth-child(1) > div > div.nrc6-wrapper > div > div.nrc6-content-section > div.nrc6-main > div > ol > li:nth-child(1) > div > div > div.VY2U > div.vmXl.vmXl-mod-variant-large > span:nth-child(1)
##listWrapper > div > div:nth-child(2) > div > div:nth-child(1) > div > div.nrc6-wrapper > div > div.nrc6-content-section > div.nrc6-main > div > ol > li:nth-child(1) > div > div > div.VY2U > div.c_cgF.c_cgF-mod-variant-full-airport > div > div:nth-child(1) > span > span:nth-child(1)
##listWrapper > div > div:nth-child(2) > div > div:nth-child(1) > div > div.nrc6-wrapper > div > div.nrc6-content-section > div.nrc6-main > div > ol > li:nth-child(1) > div > div > div.VY2U > div.c_cgF.c_cgF-mod-variant-full-airport > div > div:nth-child(3) > span > span:nth-child(1)
##listWrapper > div > div:nth-child(2) > div > div:nth-child(1) > div > div.nrc6-wrapper > div > div.nrc6-content-section > div.nrc6-main > div > ol > li:nth-child(1) > div > div > div.JWEO > div.vmXl.vmXl-mod-variant-default > span
#'something_outbound': item.select_one('div > ol > li:nth-child(1)').text,