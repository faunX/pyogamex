#!/usr/bin/env python3
import firebase_admin 
from firebase_admin import credentials
from firebase_admin import firestore
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

cred  = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

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
	driver.get("https://vega.ogamex.net/galaxy")
	time.sleep(1)

	gal = driver.find_element_by_id("galaxyInput")
	valu = driver.find_element_by_id("systemInput")
	secs = (float(random.randint(50, 70))/50)

	for i in range(1,6):
		gal.clear()
		gal.send_keys(i) #setting galaxy_number in input

		for j in range(1,500):
			valu.send_keys(Keys.BACKSPACE)
			valu.send_keys(Keys.BACKSPACE)
			valu.send_keys(Keys.BACKSPACE)

			time.sleep(secs)

			valu.send_keys(j) #setting system_number in input
			valu.send_keys(Keys.ENTER)

			time.sleep(secs)
			pagesource = driver.page_source
			soup = BeautifulSoup(pagesource, 'html.parser')
			info = soup.find_all('div', class_="galaxy-col col-player")
			#moon = soup.find_all('div',class_="galaxy-col col-moon")
			planet = soup.find_all('div',class_="galaxy-col col-planet-index")
			vega = soup.find_all('div', class_="galaxy-col col-alliance")
			for k in range(15): #search every planet
				# # Extract & Save Timestamp System, Galaxy, Position and PlayerName
				#galaxy.append(i)
				#system.append(j)
				#planet_no.append(planet[k].find('span').get_text())
				#player.append(info[k].find('span').get_text())
				#status = info[k].find('span',{'class':['isInactive28 tooltip','isInactive7 tooltip', 'isVacation tooltip', 'isNoob tooltip']})
				
				rankCompare = 0
				r = info[k].find('span').get('data-tooltip-content')
				if r:
					r = BeautifulSoup(r, 'html.parser')
					r = r.find('a', class_="galaxy-shortcut-action")
					rankCompare = int(r.get_text().replace(".",""))
				
				
				if rankCompare <= 20 and rankCompare >= 1:
					if info[k].find('span').get_text() != "":
						print("")
						print("Galaxy: " + str(i) + " - System: " + str(j) + " - Position: " + planet[k].find('span').get_text())
						today = datetime.date.today()
						db.collection('player_coords_' + str(today)).add({'player_name':info[k].find('span').get_text(), 
						'galaxy_number':i, 
						'system_number':j, 
						'position_number': planet[k].find('span').get_text()})

	driver.quit()
	display.stop()