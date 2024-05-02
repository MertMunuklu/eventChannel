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

def eventMag():
    response = requests.get("https://eventmag.co/")
    soup = BeautifulSoup(response.content, 'html.parser')
    headings = soup.find_all('h5')
    for heading in headings:
        print(heading.text)


def biletiniAl():
    response = requests.get("https://biletinial.com/tr-tr/tiyatro/istanbul-avrupa")
    soup = BeautifulSoup(response.content, 'html.parser')
    names = soup.find_all('a')
    for name in names:
        print(name.text)
    