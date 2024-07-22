from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import requests
import unicodedata

def turkce_ingilizce_cevir(metin):
    turkce_karakterler = "çğıöşüÇĞİÖŞÜ"
    ingilizce_karakterler = "cgiosuCGIOSU"
    cevirici = str.maketrans(turkce_karakterler, ingilizce_karakterler)
    return metin.translate(cevirici)
class eventMagScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
    
    def scrape_all(self,a):

        self.driver.get("https://eventmag.co/kategori/istanbul/")
        count = 0
        window_height = self.driver.execute_script("return window.innerHeight;")
        the_event_title_list = []
        the_event_type_list = []
        the_date_and_the_place_list = []
        the_list_of_lists = []
        for i in range(1,a+1):
            count += 1
            the_event_title = self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//*[@id='primary']/div/div/div[2]/div[{i}]/div[1]/div[2]/h5")))
            the_event_title_list.append(the_event_title.text)
            the_event_type = self.wait.until(EC.visibility_of_element_located((By.XPATH,f"//*[@id='primary']/div/div/div[2]/div[{i}]/div[1]/div[2]/h6")))
            the_event_type_list.append(the_event_type.text)
            the_date_and_the_place = self.wait.until(EC.visibility_of_element_located((By.XPATH,f"//*[@id='primary']/div/div/div[2]/div[{i}]/div[1]/div[3]")))                
            the_date_and_the_place_list.append(the_date_and_the_place.text)
            if (i == 8 or  i==16 or i == 20 or i == 22 or i == 28 or i == 34):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Sayfanın en sonuna scroll et
                sleep(2)  
    
        dates = []
        places = []

        for i in the_date_and_the_place_list:
            date , place = i.split("\n",1)
            dates.append(date)
            places.append(place)

        the_list_of_lists = [(a,b,c,d) for a,b,c,d in zip(the_event_title_list,the_event_type_list,dates,places)]
        self.driver.quit()
        return the_list_of_lists
        