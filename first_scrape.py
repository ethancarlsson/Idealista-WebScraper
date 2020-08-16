import requests
import time
import selenium
from selenium import webdriver
import csv
import itertools

search = str(input('Paste the url of your idealista search here: '))
pages = int(input('How many pages do you want to scrape after the first? '))

url_txt = open('the_url.txt', 'w')
url_txt.write(search)
url_txt.close()

driver = webdriver.Chrome(r'C:\Users\LENOVO\Desktop\chromedriver.exe')
driver.get(search)

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
        except selenium.common.exceptions.NoSuchElementException:
            price = 'price not found'
        
        try:
            size = driver.find_element_by_xpath('//*[@id="main-content"]/section/article[{}]/div/span[1]'.format(x)).text
            if size == '1 hab.':
                size = driver.find_element_by_xpath('//*[@id="main-content"]/section/article[{}]/div/span[2]'.format(x)).text
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

driver.execute_script("window.scrollTo(0, 8000)")
time.sleep(1)

count = 3
for _ in range(pages):
    try:
        page_2 = driver.find_element_by_xpath(f'//*[@id="main-content"]/section/div/ul/li[{count}]/a')
        count+=1
        change_page = page_2.get_attribute('href')
        driver.quit()
        driver = webdriver.Chrome(r'C:\Users\LENOVO\Desktop\chromedriver.exe')
        driver.get(change_page)


        for i in range(31):
            try:
                x=1+i
                titles = driver.find_elements_by_xpath('//*[@id="main-content"]/section/article[{}]/div/a'.format(x))
                try:
                    price = driver.find_element_by_xpath('//*[@id="main-content"]/section/article[{}]/div/div[1]/span'.format(x)).text
                except selenium.common.exceptions.NoSuchElementException:
                    price = 'price not found'
                
                try:
                    size = driver.find_element_by_xpath('//*[@id="main-content"]/section/article[{}]/div/span[1]'.format(x)).text
                    if size == '1 hab.':
                        size = driver.find_element_by_xpath('//*[@id="main-content"]/section/article[{}]/div/span[2]'.format(x)).text
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
    except: 
        pass




driver.quit()


transposer = [rent_description, prices, sizes, cheapest_rents]
transposed_list = list(map(list, zip(*transposer)))


outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
for row in transposed_list:
    outputWriter.writerow(row)


outputFile.close()


