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
        'name': get_value(bs_exhibitor, 'div', 'popup-name ng-binding'),
        'description': get_value(bs_exhibitor, 'div', 'popup-desc ng-binding ng-scope'),
        'hall': get_value(bs_exhibitor, 'span', 'popup-stand-text ng-binding'),
        'address': get_value(bs_exhibitor, 'div', 'popup-street ng-binding'),
        'number': get_value(bs_exhibitor, 'div', 'popup-phone ng-binding'),
        'email': get_value(bs_exhibitor, 'div', 'popup-email'),
        'web': get_value(bs_exhibitor, 'a', 'underline-animation ng-binding'),
    }

def get_value(bs: BeautifulSoup, tag: str, class_: str) -> str:
    tag = bs.find(tag, class_)
    return tag.text.strip()


if __name__ == '__main__':
    main()