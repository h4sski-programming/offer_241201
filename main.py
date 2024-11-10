import requests
from bs4 import BeautifulSoup

def main():
    base_url = 'https://www.amcham.org.eg/membership/members-database?keyword=&keywordtype=company&sector=0&subsector=0&membershiptype=0'
    r = requests.get(base_url, verify=False)
    bs = BeautifulSoup(r.content)
    
    phone_div = bs.div(class_='popup-phone')
    phone = str(phone_div).split('{{')[1].split('}}')[0]
    print(phone)
    
    # p = bs.find_all('div', 'exhibitors-main-container')
    # for pp in p:
    #     print(pp['url'])


if __name__ == '__main__':
    main()