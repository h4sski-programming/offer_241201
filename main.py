import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver

def main():
    driver = webdriver.Chrome()
    # driver.implicitly_wait(2)
    # base_url = 'https://www.amcham.org.eg/membership/members-database?keyword=&keywordtype=company&sector=0&subsector=0&membershiptype=0'
    base_url = 'https://www.selenium.dev/selenium/web/web-form.html'
    
    driver.get(base_url)
    # time.sleep(10)
    
    # page_source = driver.page_source
    print(driver.test)
    
    # r = requests.get(base_url, verify=False)
    
    # bs = BeautifulSoup(page_source, 'html.parser')
    
    # item = bs.div(class_='thumbnail thumbnail-news')
    # data = item
    # print(data)
    
    # p = bs.find_all('div', 'exhibitors-main-container')
    # for pp in p:
    #     print(pp['url'])
    
    driver.quit()


if __name__ == '__main__':
    main()