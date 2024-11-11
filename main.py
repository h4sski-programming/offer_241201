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
    
    wystawcy = bs.find_all('div', 'exhibitors-main-container ng-scope')
    url_wystawcow = []
    for w in wystawcy[:2]:
        number = w.get('url').split('/')[-1]
        url_wystawcow.append('/'.join([base_url, number]))
    
    print(url_wystawcow)
    
    # item = bs.div(class_='thumbnail thumbnail-news')
    # data = item
    # print()
    
    # p = bs.find_all('div', 'thumbnail thumbnail-news')
    # p = bs.find_all('a', 'more dot ddd-keep')
    # for pp in p:
    #     print(pp)
    
    driver.quit()


if __name__ == '__main__':
    main()