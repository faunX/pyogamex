import time
from selenium import webdriver

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
driver.get("https://vega.ogamex.net/fleet?planet=99c17658-c369-4213-8079-e89bd7127dd7")

time.sleep(1)

allLinksShips = driver.find_element_by_tag_name("a")
i = 0
while i < len(allLinksShips):
    print(allLinksShips[i])
    i = i+1