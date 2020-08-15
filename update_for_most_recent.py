import requests
import time
import selenium
from selenium import webdriver
import csv
import os
import datetime

most_recent = str(input('It is recomended that you use the "most recent" search on idealista for this scraper. Would you like to use the URL from your "first_scrape"? (y/n) '))
if most_recent == 'y':
    url_txt = open('the_url.txt', 'r')
    url = url_txt.read()
else:
    url = input('Input your new search URL: ')
    
driver = webdriver.Chrome(r'C:\Users\LENOVO\Desktop\chromedriver.exe')
driver.get(url)

url = driver.current_url

cheapest_rents = []
rent_description = []
prices = []
sizes = []

for i in range(31):
    try:
        x=1+i
        titles = driver.find_elements_by_xpath('//*[@id="main-content"]/section/article[{}]/div/a'.format(x))
        try:
            price = driver.find_element_by_xpath('//*[@id="main-content"]/section/article[{}]/div/div[1]/span'.format(x)).text
            price.rstrip('€/mes')
        except selenium.common.exceptions.NoSuchElementException:
            price = 'price not found'
        
        try:
            size = driver.find_element_by_xpath('//*[@id="main-content"]/section/article[{}]/div/span[1]'.format(x)).text
            if size == '1 hab.':
                size = driver.find_element_by_xpath('//*[@id="main-content"]/section/article[{}]/div/span[2]'.format(x)).text
                size.rstrip('m²')
            else:
                pass
        except selenium.common.exceptions.NoSuchElementException:
            price = 'size not found'        

        print(titles[0].text)
        print(price)
        print(size)
        print(titles[0].get_attribute('href'))
        cheapest_rents.append(titles[0].get_attribute('href'))
        rent_description.append(titles[0].text)
        prices.append(price)
        sizes.append(size)
    except IndexError:
        pass


driver.quit()


transposer = [rent_description, prices, sizes, cheapest_rents]
transposed_list = list(map(list, zip(*transposer)))


newPlacesFile = open('new_output.csv', 'w', newline='')
newPlacesWriter = csv.writer(newPlacesFile)
for row in transposed_list:
    newPlacesWriter.writerow(row)

newPlacesFile.close()


output = []
new_output = []

outputFile = open('output.csv', 'r')

for line in csv.reader(outputFile):
    output.append(tuple(line))

outputFile.close()

new_outputFile = open('new_output.csv', 'r')

for line in csv.reader(new_outputFile):
    new_output.append(tuple(line))

outputFile.close()

set1 = set(output)
set2 = set(new_output)
x = set2 - set1
print(x) # everything plus the new things

everything_finished = list(set1.union(x))
new_rents = list(x)

output = open('output.csv', 'w', newline='')
outputWriter = csv.writer(output)
for row in everything_finished:
    outputWriter.writerow(row)

today = datetime.datetime.now()

time = today.strftime('%d%b%H%p')

new_places = open('new_places{}.csv'.format(time), 'w', newline='')
outputWriter = csv.writer(new_places)
for row in new_rents:
    outputWriter.writerow(row)

new_places.close()
output.close()
