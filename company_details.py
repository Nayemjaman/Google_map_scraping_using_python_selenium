import csv
import time
import os
from selenium.common.exceptions import StaleElementReferenceException
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import re


class CompanyDetailScraper:

    def __init__(self):
        # self.panel_xpath = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]'
        self.panel_xpath = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]'
        self.business_list = []
        self.business_info = {}
        self.verbose = None
        self.headless = False
        self.driver = None
        self.d_id = 0
        self.unique_check = []

    def config_driver(self):
        options = Options()
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-setuid-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--start-maximized")
        options.add_argument("--window-size=1920,1080")
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s, options=options)

        self.driver = driver

    def save_data(self, data):
        header = ['companey_name', 'address', 'companey_category', 'contact', 'website', 'detail_url','latitude', 'longitude', 'img_src', 'rating', 'reviews_count',]
        with open('data.csv', 'a', newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            if csvfile.tell() == 0:  
                writer.writerow(header)
            writer.writerow(data)


    
    def get_company_detail(self, url):
        self.driver.get(url)


        try:
            companey_name = self.driver.find_element(By.CLASS_NAME, "lfPIob").text
            if len(companey_name.split(' ')) >1:
                companey_name = ''.join(companey_name)
            else:
                companey_name = companey_name
        except:
            companey_name = ' '
        # print(companey_name,"***********")
        try:
            a = self.driver.find_element(By.CLASS_NAME, "skqShb").text
        except:
            a = ' '
        
        match = a.split()


        # print(match)

        if len(match)> 2:
            rating = match[0]
            reviews_count = match[1]
            reviews_count = reviews_count[1:-1]
        else:
            rating = ' '
            reviews_count = ' '
           
        # print(rating)
        # print(reviews_count)
        try:
            companey_category = self.driver.find_element(By.CLASS_NAME, "skqShb .DkEaL").text
        except:
            companey_category = ' '
        # print(companey_category)
        try:
            address = self.driver.find_element(By.CLASS_NAME, "kR99db").text
        except:
            address = ' '
        # print(address,"address")
        try:
            website = self.driver.find_element(By.CLASS_NAME, "lcr4fd").get_attribute("href")
        except:
            website = " "
        # print(website,"website")
        try:
            contact = self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label^="Phone"]').text
        except:
            contact = " "
        try:
            image_element = self.driver.find_element(By.CLASS_NAME, "lvtCsd img")
            img_src = image_element.get_attribute('src')

        except:
            img_src = " "
        # print("image link")
        # print(img_src)

        time.sleep(3)
        detail_url = self.driver.current_url
        # print(detail_url)
        match = re.search(r'@(-?\d+\.\d+),(-?\d+\.\d+)', detail_url)
        if match:
            latitude = match.group(1)
            longitude = match.group(2)
        else:
            latitude = " "
            longitude = " "
        # print(longitude)            
        # print(latitude)    
        data = [companey_name, address, companey_category, contact, website, detail_url,latitude, longitude, img_src, rating, reviews_count,]
        self.save_data(data)     







CompanyDetail = CompanyDetailScraper()
CompanyDetail.config_driver()
with open("company_urls.txt", "r") as f:
    urls = f.readlines()
urls = [x.strip() for x in urls]
for i in range(0, (len(urls))):
    url = urls[i]
    CompanyDetail.get_company_detail(url)