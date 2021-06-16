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
	driver.get("https://vega.ogamex.net/fleet")

	time.sleep(1)

	print(driver.current_url)

	contentDiv = driver.find_element_by_class_name("content")
	allShipsDiv = contentDiv.find_elements_by_xpath("//div[@class='ship-item tooltip']")

	expoWaves = 2
	shipsSend = 0
	shipName = "FALCON"

	for div in allShipsDiv:
		shipBtn = div.find_element_by_class_name("ship-btn")
		if shipBtn.get_attribute("data-ship-type") == shipName:
			inputFalcon = div.find_element_by_tag_name("input")
			maxShips = int(inputFalcon.get_attribute("max-ships"))
			shipsSend = int(maxShips / expoWaves)
			print(shipsSend)

	#expo bot
	i = 0
	while i < 100:
		try:
			while expoWaves > 0:
				driver.get("https://vega.ogamex.net/fleet")
				time.sleep(1)

				contentDiv = driver.find_element_by_class_name("content")
				allShipsDiv = contentDiv.find_elements_by_xpath("//div[@class='ship-item tooltip']")

				for div in allShipsDiv:
					shipBtn = div.find_element_by_class_name("ship-btn")
					if shipBtn.get_attribute("data-ship-type") == shipName:
						inputFalcon = div.find_element_by_tag_name("input")
						inputFalcon.send_keys(shipsSend)
						next1 = driver.find_element_by_id("btn-next-fleet2")
						next1.click()

						time.sleep(2)
						position = 16

						positionZ = driver.find_element_by_id("fleet2_target_z")

						positionZ.send_keys(position)

						next2 = driver.find_element_by_id("btn-next-fleet3")
						next2.click()

						print("flota pantalla 3")

						time.sleep(2)

						next3 = driver.find_element_by_id("btn-submit-fleet")
						next3.click()

						print("FINISH")
				    		
				expoWaves = expoWaves - 1
				time.sleep(3)
			i = i+1
			time.sleep(3600)
		except Exception:
			continue



		    		
		
		
