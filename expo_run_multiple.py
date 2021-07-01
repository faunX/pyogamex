#!/usr/bin/env python3

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
	driver.get("https://ogamex.net/connect?serverId=2f965194-a236-41b9-8807-6bcc8e6aa734")

	time.sleep(1)


	
	#expo bot
	i = 0
	while i < 100:
		try:
			driver.get("https://vega.ogamex.net/fleet/autoexpedition")

			print(driver.current_url)


			unitContainer = driver.find_element_by_class_name("unit-container")
			divFalcons = unitContainer.find_element_by_xpath("//div[@data-ship-type='FALCON']")
			allFalconsButton = divFalcons.find_element_by_class_name("btn-unit-full")
			allFalconsName = divFalcons.find_element_by_class_name("unit-title")

			allFalconsButton.click()

			print(allFalconsName)

			btnSend = driver.find_element_by_id("btnSend")
			btnSend.click()

			time.sleep(3)
			print(i)
			i = i+1
			time.sleep(3600)
		except Exception as e:
			print(e)
			time.sleep(900)
			continue



		    		
		
		
