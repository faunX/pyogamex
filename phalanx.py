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
import threading

'''
def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t
'''

galaxy = "4"
system = "357"

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
	element.send_keys("ramiropadrog@gmail.com")
	element = driver.find_element_by_name("Password")
	element.send_keys("rami38050222")

	element = driver.find_element_by_id("btnLogin")
	element.click()
	time.sleep(2)
	#end login

	driver.get("https://ogamex.net/connect?serverId=78e96ca5-97dc-4eb0-b4bc-73f72da3df7b") #titan
	driver.get("https://titan.ogamex.net/galaxy?x=" + galaxy + "&y=" + system)
	time.sleep(1)

	while 1 == 1:
		container = driver.find_element_by_class_name("galaxy-info")
		objetive_planet = container.find_element_by_xpath("//div[@class='galaxy-col col-planet-name']")
		
		btn_phx = objetive_planet.find_element_by_class_name("fa-satellite-dish")
		btn_phx.click()
		sensorFleetMovements = driver.find_element_by_class_name("fleet-movement-wrapper")
		tableMovements = sensorFleetMovements.find_element_by_id("fleet-movement-table")
		
		if tableMovements == null: 
			print("error")
			break
		
		time.sleep(1)
		driver.get("https://titan.ogamex.net/galaxy?x=" + galaxy + "&y=" + system)
		time.sleep(2)
		print(1)

	driver.quit()
	display.stop()