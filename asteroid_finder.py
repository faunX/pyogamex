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

display = Display(visible=0, size=(1024, 768))
display.start()
if __name__ == "__main__":
	path = ""

	email = ("ramiropadrog@gmail.com")

	password = ("rami38050222")

	options = webdriver.ChromeOptions()
	options.add_argument('--no-sandbox')
	driver = webdriver.Chrome(options=options)
	driver.get("https://ogamex.net/#")
	element = driver.find_element_by_xpath('//*[@id="bodyWrapper"]/footer/div/div[2]/a[2]')
	element.click()
	element = driver.find_element_by_name("Email")
	element.send_keys(email)
	element = driver.find_element_by_name("Password")
	element.send_keys(password)

	element = driver.find_element_by_id("btnLogin")
	element.click()
	time.sleep(2)

	#filling variables

	driver.get("https://ogamex.net/connect?serverId=4c0057df-6571-4089-818d-e6d8ca1bd992") #nova
	driver.get("https://nova.ogamex.net/galaxy?x=2&y=1")

	time.sleep(1)

	gal = driver.find_element_by_id("galaxyInput")
	valu = driver.find_element_by_id("systemInput")

	for j in range(1,499):
		valu.send_keys(Keys.BACKSPACE)
		valu.send_keys(Keys.BACKSPACE)
		valu.send_keys(Keys.BACKSPACE)

		valu.send_keys(j) #setting system_number in input
		valu.send_keys(Keys.ENTER) #select next system

		time.sleep(2)
		slots = driver.find_elements_by_class_name("galaxy-item") #each inactive is a row
		slotsLen = len(slots)
		if len(slots) >= 18:
			asteroidPosition = slots[slotsLen - 1]
			asteroidDivs = asteroidPosition.find_elements_by_tag_name('div')
			if len(asteroidDivs) <= 3:
				print("coords: 1 - " + str(j))

	driver.quit()
	display.stop()