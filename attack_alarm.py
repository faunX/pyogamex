import constants
from pandas import DataFrame
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions
import requests
import time
import random
from selenium import webdriver
import platform
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import decimal
from pyvirtualdisplay import Display
from playsound import playsound


display = Display(visible=0, size=(1024, 768))
display.start()
if __name__ == "__main__":
	path = ""

	#login
	options = webdriver.ChromeOptions()
	options.add_argument('--no-sandbox')
	driver = webdriver.Chrome(options=options)
	driver.get("https://ogamex.net/#")
	element = driver.find_element_by_xpath('//*[@id="bodyWrapper"]/footer/div/div[2]/a[2]')
	element.click()
	element = driver.find_element_by_name("Email")
	element.send_keys(constants.EMAIL)
	element = driver.find_element_by_name("Password")
	element.send_keys(constants.PASSWORD)

	element = driver.find_element_by_id("btnLogin")
	element.click()
	time.sleep(2)
	#end login

	driver.get("https://ogamex.net/connect?serverId=" + constants.VEGA_ID) #vega
	time.sleep(5)


	pagesource = driver.page_source
	soup = BeautifulSoup(pagesource, 'html.parser')
	allPlanetsUnderAttack = soup.find_all('div', {'class':["planet-item underAttack", "planet-item underAttack selected"]})
	print(len(allPlanetsUnderAttack))

	while len(allPlanetsUnderAttack) > 0:
		allPlanetsUnderAttack = soup.find_all('div', {'class':["planet-item underAttack", "planet-item underAttack selected"]})
		print(len(allPlanetsUnderAttack))
		playsound("./alarm-sound.WAV")
