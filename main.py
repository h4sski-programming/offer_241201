import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

def main():
    service = Service("/snap/bin/geckodriver")
    driver = webdriver.Firefox(service=service)
    # driver.implicitly_wait(5)
    base_url = 'https://www.amcham.org.eg/membership/members-database?keyword=&keywordtype=company&sector=0&subsector=0&membershiptype=0'
    
    driver.get(base_url)
    time.sleep(7)
    
    title = driver.title
    print(title)
    
    ######################################
    
    page_source = driver.page_source
    
    bs = BeautifulSoup(page_source, 'html.parser')
    
    item = bs.div(class_='thumbnail thumbnail-news')
    data = item
    print(data)
    
    # p = bs.find_all('div', 'exhibitors-main-container')
    # for pp in p:
    #     print(pp['url'])
    
    driver.quit()


if __name__ == '__main__':
    main()