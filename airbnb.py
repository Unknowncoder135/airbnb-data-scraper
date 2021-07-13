


# driver.page_scroce
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
import wget


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get('https://www.airbnb.co.in/s/all?refinement_paths%5B%5D=%2Fhomes&query=goa')
time.sleep(1)
try:
    mm = driver.find_element_by_class_name('_1xiwgrva').click()
except:
    pass

main_list  = []
df = pd.DataFrame({'resort_name':[''], 'price':[''], 'rateing':[''], 'discription':[''],'links':['']})
while True:
    main = driver.find_element_by_class_name('_fhph4u')
    main_div = main.find_elements_by_class_name('_1kmzzkf')
    for x in main_div:
        name = x.find_element_by_class_name('_5kaapu').text
        price = x.find_element_by_class_name('_1gi6jw3f').text
        try:
            rateing  = x.find_element_by_class_name('_10fy1f8').text
        except:

            rateing = "no rating"
        discription = x.find_element_by_class_name('_3c0zz1').text
        links = x.find_element_by_class_name('_mm360j').get_attribute('href')
        # main_dir = {
        #     'resort_name',name,
        #     'price',price,
        #     'rateing',rateing,
        #     'discription',discription,
        #     'links',links,
        # }
        df = df.append({'resort_name': name, 'price': price, 'rateing': rateing, 'discription': discription, 'links': links},
        ignore_index= True)

    print(main_list)
    try:
        next_page = driver.find_element_by_css_selector('a[aria-label="Next"]').get_attribute('href')
        driver.get(next_page)
    except:
        print('all data scraped')
        break
    

df.to_csv('data-demo.csv',index=False)
driver.close()
