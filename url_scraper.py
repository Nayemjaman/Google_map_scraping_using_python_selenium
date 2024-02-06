import time
import os
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class UrlScraper:
    def __init__(self):
        self.headless = False
        self.driver = None
        self.panel_xpath = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]'

    def config_driver(self):
        options = Options()
        options.add_argument("--start-maximized")
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s, options=options)

        self.driver = driver

    def get_keyword_city(self):
        with open("keywords.txt", "r") as f:
            keywords = f.readlines()
        keywords = [x.strip() for x in keywords]
        print(keywords)
        with open("division.txt", "r") as f:
            divisions = f.readlines()
        divisions = [x.strip() for x in divisions]
        print(divisions)

        self.driver.get("https://www.google.com/maps?hl=en")
        time.sleep(2)
        for division in divisions:
            for keyword in keywords:
                search_query = f"{keyword} in {division}"
                print(search_query)
                search_box = self.driver.find_element(
                    By.XPATH, '//*[@id="searchboxinput"]')
                search_box.send_keys(search_query)
                search_box.send_keys(Keys.ENTER)
                time.sleep(1)
                self.scroll_companies()

                search_box.clear()

    def get_url(self):
        company_urls = self.driver.find_elements(By.CLASS_NAME, "hfpxzc")
        unique_urls = set()  # Create a set to store unique URLs

        for company_url in company_urls:
            url = company_url.get_attribute("href")
            unique_urls.add(url)  # Add the URL to the set
        if not os.path.exists("company_urls.txt"):
            open("company_urls.txt", "w").close()
        with open("company_urls.txt", "r") as f:
            existing_urls = set(line.strip() for line in f)

        with open("company_urls.txt", "a") as fa:
            for url in unique_urls - existing_urls:
                fa.write(url + "\n")  # Write the unique URLs to the file

    def scroll_companies(self):
        time.sleep(10)
        scrollable_div = self.driver.find_element(By.XPATH, self.panel_xpath)
        # scrolling
        flag = True
        i = 0
        while flag:
            print(f"Scrolling to page {i + 2}")
            self.driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollHeight', scrollable_div)
            time.sleep(2)

            if "You've reached the end of the list." in self.driver.page_source:
                flag = False

            self.get_url()
            i += 1


url_collect = UrlScraper()
url_collect.config_driver()
url_collect.get_keyword_city()
