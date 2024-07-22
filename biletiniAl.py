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

class biletiniAl:
    def __init__(self):
        self.response = requests.get("https://biletinial.com/tr-tr/sinema/istanbul-avrupa")
        self.soup = BeautifulSoup(self.response.content, 'html.parser')
        self.namesS = []
    def scrape_cinema(self,date):
        self.response = requests.get(f"https://biletinial.com/tr-tr/sinema/istanbul-avrupa?date=2024-05-{date}&filmtypeid=0&loc=0&thisweekend=")
        self.soup = BeautifulSoup(self.response.content, 'html.parser')
        names = self.soup.find_all('h3')
        for name in names:
            self.namesS.append(name.text)
        return self.namesS

    def take_sessions(self,movie):
        self.mainurlwithfilm = "https://biletinial.com/tr-tr/sinema/"
        index = self.namesS.index(movie)
        self.the_movie_str = self.namesS[index]
    
    def movie_descriptions(self, movie):
        mert = turkce_ingilizce_cevir(movie.lower().replace(" ", "-"))
        url_movie = f"https://biletinial.com/tr-tr/sinema/{mert}"
        self.response = requests.get(url_movie)
        self.soup = BeautifulSoup(self.response.content, 'html.parser')
        desc = self.soup.find(
            'div', class_="yds_cinema_movie_thread_info"
        ).text.strip()
        details = self.soup.find(
            'div', class_="yds_cinema_movie_thread_detail"
        ).text.strip()
        return desc, details