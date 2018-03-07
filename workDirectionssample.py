#!python3
#workDirectionsSample.py


#import selenium and datetime modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import datetime
import time

#Set specific work day that you want reminder  for.
#Code sleeps every second until after time set in workDay variable
workDay = datetime.datetime(2017,11,28,6,55,0)#Enter date and time you want the program to start.

while datetime.datetime.now() < Workday:
    time.sleep(1)



#Initialize Chrome browser and navigate to google maps
driver = webdriver.Chrome(r"Enter path of chromedriver or different driver you want to use")
driver.get('https://www.maps.google.com')
searchBar = driver.find_element_by_xpath('//*[@id="searchboxinput"]')
searchBar.click()

#Type in address you want directions too. 
searchBar.send_keys('Enter address here')
searchElem = driver.find_element_by_xpath('Enter xpath here')
searchElem.click()

#Wait until search bar is visible
driver.implicitly_wait(15)

elem1 = driver.find_element_by_xpath('//*[@id="pane"]/div/div[2]/div/div/div[1]/button[2]/div/div')
elem1.click()
startFrom = driver.find_element_by_xpath('//*[@id="sb_ifc51"]/input')
startFrom.click()
startFrom.send_keys('Enter address your starting from')
directions = driver.find_element_by_xpath('//*[@id="directions-searchbox-0"]/button[1]')
directions.click()
#select first itinerary which is by default the fastest route
fastestRoute = driver.find_element_by_xpath('//*[@id=":3"]')
fastestRoute.click()
elem2 = driver.find_element_by_xpath('//*[@id=":0"]/div')
elem2.click()
elem3 = driver.find_element_by_xpath('//*[@id="section-directions-trip-0"]/div[2]/div[1]/div[2]/h1[1]/span')
elem3.click()
elem4 = driver.find_element_by_xpath('//*[@id="pane"]/div/div[2]/div/div/div[2]/div[3]/div[1]/button')
elem4.click()
#Sign in button
signIn = driver.find_element_by_xpath('//*[@id="pane"]/div/div[2]/div/div/div[2]/div[3]/div[1]/div/div/button')
signIn.click()
userName = driver.find_element_by_xpath('//*[@id="identifierId"]')
userName.click()

#Type in Google username
userName.send_keys('type in username')
elemNext = driver.find_element_by_xpath('xpath for "next button" ')
elemNext.click()
driver.implicitly_wait(20)

#Type in Google password
elemPass = driver.find_element_by_xpath('xpath for password box)
elemPass.send_keys('type in password')
elemNext2 = driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span')
elemNext2.click()
#Send a text to the phone number in your google profile with link to directions with fastest route
sendText = driver.find_element_by_xpath('//*[@id="modal-dialog-widget"]/div[2]/div/div[3]/div/div/div[2]/div[3]/div/div[1]/span[3]/span[1]/button')
sendText.click()
