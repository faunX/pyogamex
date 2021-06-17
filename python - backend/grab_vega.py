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
    driver.get("https://ogamex.net/connect?serverId=2f965194-a236-41b9-8807-6bcc8e6aa734")
#    driver.get("https://ogamex.net/connect?serverId=1d81dce5-163a-4947-ad9c-c354f5f2220e")
    driver.get("https://vega.ogamex.net/galaxy")
#    driver.get("https://beta.ogamex.net/galaxy")
    time.sleep(1)
    moon_data = []
    player = []
    planet_no = []
    galaxy = []
    system = []
    aliance = []
    moon_time = []
    planet_time = []
    timestamp = []
    alliance = []
    ranking = []
    s = []
    text_file = open("debug", "w")
    text_file.write(driver.page_source)
    text_file.close()
    gal = driver.find_element_by_id("galaxyInput")
    valu = driver.find_element_by_id("systemInput")
    secs = (float(random.randint(50, 70))/50)

    for i in range(1,6):
        gal.clear()
        gal.send_keys(i)

        for j in range(1,500):
            valu.send_keys(Keys.BACKSPACE)
            valu.send_keys(Keys.BACKSPACE)
            valu.send_keys(Keys.BACKSPACE)
            time.sleep(secs)
            valu.send_keys(j)
            valu.send_keys(Keys.ENTER)
            print(f"Galaxy: {i}")
            print(f"System: {j}")
            print(f"Mapping took {secs} seconds")
            time.sleep(secs)
            pagesource=driver.page_source
            soup = BeautifulSoup(pagesource, 'html.parser')
            info = soup.find_all('div', class_="galaxy-col col-player")
            moon = soup.find_all('div',class_="galaxy-col col-moon")
            planet = soup.find_all('div',class_="galaxy-col col-planet-index")
            vega = soup.find_all('div', class_="galaxy-col col-alliance")
            for k in range(15): #search every planet
                # # Extract & Save Timestamp System, Galaxy, Position and PlayerName
                # timestamp.append( datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                galaxy.append(i)
                system.append(j)
                planet_no.append(planet[k].find('span').get_text())
                player.append(info[k].find('span').get_text())

                # Extract & Save Ranking
                r = info[k].find('span').get('data-tooltip-content')
                if r:
                    r = BeautifulSoup(r, 'html.parser')
                    r = r.find('a', class_="galaxy-shortcut-action")
                    ranking.append(r.get_text())
                else:
                    ranking.append(" ")

                # Extract & Save Player Status
                status = info[k].find('span',{'class':['isInactive28 tooltip','isInactive7 tooltip']})
                if status is not None:
                    if status.get_text() == "I" or status.get_text() == "i":
                        s.append(status.get_text() + "nactive")
                    else:
                        s.append(status.get_text() + ", Active")
                else:
                    s.append("Active")

                # Extract & Save Alliance
                z = vega[k].find('span')
                if z is not None:
                    alliance.append(z.get_text())
                else:
                    alliance.append("none")

                # Extract & Save Moon Details
                div1 = moon[k].find('div')
                if div1:
                    div2 = div1.find('div')
                    if div2:
                        if div2.get_text():
                            moon_time.append(div2.get_text())
                        else:
                            moon_time.append("Playing Now")
                    else:
                        moon_time.append("Offline")
                    moon_data.append("Yes")
                else:
                    moon_data.append("No")
                    moon_time.append("Offline")

                # Extract & Save Planet Details
                div3 = planet[k].find('div')
                if div3:
                    div4 =div3.find("div")
                    if div4:
                        if div4.get_text():
                            planet_time.append(div4.get_text())
                        else:
                            planet_time.append("Playing Now")
                    else:
                        planet_time.append("Offline")
                else:
                    planet_time.append("Offline")

    data = {'Timestamp': timestamp, 'Galaxy':galaxy, 'System':system,'Planet#':planet_no, 'Planet Time': planet_time, 'Moon': moon_data,
    'Moon Time': moon_time, 'Player': player, 'Alliance': alliance, 'Status': s }
    df = pd.DataFrame(data)
    df.to_csv("vega-latest.csv")
    driver.quit()
    display.stop()