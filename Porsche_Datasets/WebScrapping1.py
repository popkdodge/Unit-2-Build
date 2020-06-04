from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.cars.com/for-sale/searchresults.action/?clrId=27125%2C27128%2C27129%2C29637%2C27135%2C27131&mdId=20567&mkId=20081&page=1&perPage=100&rd=99999&searchSource=GN_REFINEMENT&sort=relevance&stkTypId=28881&transTypeId=28112&yrId=20200%2C20145%2C20201%2C27381%2C34923%2C39723%2C47272%2C51683%2C56007%2C58487%2C30031936%2C35797618%2C36362520&zc=30008'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
#html_parser
page_soup = soup(page_html, 'html.parser')
#grab each product
containers = page_soup.findAll('div',{'class':'shop-srp-listings__inner'})
len(containers)
filename = 'car1other_m.csv' 


f = open(filename, 'w')
headers ='car,condition,milage,extar_info\n'
f.write(headers)
for container in containers:
    #name of car
    name_of_car = container.findAll('h2',{'class':'listing-row__title'})
    car = name_of_car[0].text.strip()
    print(car)
    #condition of car
    condition_of_car = container.findAll('div',{'class':'listing-row__stocktype'})
    condition = condition_of_car[0].text.strip()
    print(condition)
    #milage of car
    milage_of_car = container.findAll('span',{'class':'listing-row__mileage'})
    milage = milage_of_car[0].text.strip()
    print(milage)
    car_price = container.findAll('span',{'class':'listing-row__price'})
    price = car_price[0].text.strip()
    price_edit = price.replace('$','')
    price = price_edit.replace(',','')
    print(price)
    car_information = container.findAll('ul', {'class':'listing-row__meta'})
    car_info = car_information[0].text.strip().replace(' ','')
    f.write(car+','+ condition +','+milage.replace(',','')+','+price+'\n')
f.close()