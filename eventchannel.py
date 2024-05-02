from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import requests
#Take a list from the user.
def getListOfChannels(list_arg):
    if isinstance(list_arg, list):
        return list_arg
    else:
        print("Please give a list!")

def getSearchWords(word_arg):
    if isinstance(word_arg, list):
        return word_arg
    else:
        print("Please give a list.")

def kariyerNet():
    pass

#Yapraklarım suda balık gibi kıvıl kıvıl, budak budak şerhan şerhan ihtiyar bir ceviz.
def eventMag():
    driver = webdriver.Chrome()
    driver.get("https://eventmag.co/kategori/istanbul/")
    wait = WebDriverWait(driver, 10)  
    count = 0
    window_height = driver.execute_script("return window.innerHeight;")
    for i in range(1,45):
        count += 1
        the_event_title = wait.until(EC.visibility_of_element_located((By.XPATH, f"//*[@id='primary']/div/div/div[2]/div[{i}]/div[1]/div[2]/h5")))
        print(the_event_title.text)
        if (i == 8 or  i==16 or i == 20 or i == 22 or i == 28):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Sayfanın en sonuna scroll et
            sleep(2)  

    print(count)
    driver.quit()

def biletiniAl():
    response = requests.get("https://www.instagram.com/itubasinyayin/")
    soup = BeautifulSoup(response.content, 'html.parser')
    names = soup.find_all('h2')
    for name in names:
        print(name.text)

eventMag()