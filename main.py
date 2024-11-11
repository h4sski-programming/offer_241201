import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

def main():
    
    # Setup Selenium
    service = Service("/snap/bin/geckodriver")
    driver = webdriver.Firefox(service=service)
    # driver.implicitly_wait(5)
    
    # URL variable
    base_url = 'https://tsw.pl/wystawcy'
    
    # Getting the page and sleep for load all of the content
    driver.get(base_url)
    time.sleep(2)
    
    ######################################
    
    page_source = driver.page_source
    
    bs = BeautifulSoup(page_source, 'html.parser')
    
    exhibitors = bs.find_all('div', 'exhibitors-main-container ng-scope')
    url_exhibitors = []
    for w in exhibitors[:5]:
        number = w.get('url').split('/')[-1]
        url_exhibitors.append('/'.join([base_url, number]))
    
    # Debug print
    # print(url_exhibitors)
    
    exhibitors_list = []
    
    for url in url_exhibitors[:5]:
        exhibitors_list.append(get_exhibitor(driver=driver, url=url))
    
    # Debug print
    # print(exhibitors_list)
    for exh in exhibitors_list:
        print(exh['name'])
        print(exh['hall'])
        print(exh['address'])
        print(exh['email'])
        print(exh['web'])
        print('----------------')
    
    
    driver.quit()

def get_exhibitor(driver: webdriver, url: str) -> dict:
    driver.get(url)
    time.sleep(2)
    bs_exhibitor = BeautifulSoup(driver.page_source, 'html.parser')
    return {
        'name': get_name(bs_exhibitor),
        'description': get_description(bs_exhibitor),
        'hall': get_hall(bs_exhibitor),
        'address': get_address(bs_exhibitor),
        'number': get_number(bs_exhibitor),
        'email': get_email(bs_exhibitor),
        'web': get_web(bs_exhibitor),
    }

def get_name(bs: BeautifulSoup) -> str:
    div = bs.find('div', 'popup-name ng-binding')
    return div.text.strip()

def get_description(bs: BeautifulSoup) -> str:
    div = bs.find('div', 'popup-desc ng-binding ng-scope')
    return div.text.strip()

def get_hall(bs: BeautifulSoup) -> str:
    div = bs.find('span', 'popup-stand-text ng-binding')
    return div.text.strip()

def get_address(bs: BeautifulSoup) -> str:
    div = bs.find('div', 'popup-street ng-binding')
    return div.text.strip()

def get_number(bs: BeautifulSoup) -> str:
    div = bs.find('div', 'popup-phone ng-binding')
    return div.text.strip()

def get_email(bs: BeautifulSoup) -> str:
    div = bs.find('div', 'popup-email')
    return div.text.strip()

def get_web(bs: BeautifulSoup) -> str:
    div = bs.find('a', 'underline-animation ng-binding')
    return div.get('href')

if __name__ == '__main__':
    main()