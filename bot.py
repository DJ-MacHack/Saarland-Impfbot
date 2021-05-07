import requests
from selenium import webdriver
import time
from playsound import playsound

def loop(driver):
    while True:
        findSaarbrücken(driver)
        checkKeineTermine(driver)
        findSaarlouis(driver)
        checkKeineTermine(driver)
        findNeunkirchen(driver)
        checkKeineTermine(driver)
        findLebach(driver)
        checkKeineTermine(driver)
        findLebachNacht(driver)
  
def findSaarbrücken(driver):
    elementSaarbrücken = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[1]/button[1]')
    elementSaarbrücken.click()
    time.sleep(0.05)
    elementWeiter = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')
    elementWeiter.click()
    time.sleep(0.5)

def findSaarlouis(driver):
    elementSaarlouis = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[1]/button[2]')
    elementSaarlouis.click()
    time.sleep(0.05)
    elementWeiter = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')
    elementWeiter.click()
    time.sleep(0.5)

def findNeunkirchen(driver):
    elementNeunkirchen = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[1]/button[3]')
    elementNeunkirchen.click()
    time.sleep(0.05)
    elementWeiter = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')
    elementWeiter.click()
    time.sleep(0.5)

def findLebach(driver):
    elementLebach = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[1]/button[4]')
    elementLebach.click()
    time.sleep(0.05)
    elementWeiter = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')
    elementWeiter.click()
    time.sleep(0.5)

def findLebachNacht(driver):
    elementLebachNacht = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[1]/button[4]')
    elementLebachNacht.click()
    time.sleep(0.05)
    elementWeiter = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')
    elementWeiter.click()
    time.sleep(0.5)
    
def checkKeineTermine(driver):
    elementTerminNichtVerfügbar = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/h5')
    if(elementTerminNichtVerfügbar.get_attribute('innerHTML')=="Keine Termine verfügbar. "):
        elementZurück = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div/button')
        elementZurück.click()
        time.sleep(1)
    if(elementTerminNichtVerfügbar.get_attribute('innerHTML')=="Impftermine auswählen"):
        elementTable = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[1]')
        elementTermin = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[1]/div[2]/div[1]')
        elementTermin.click()
        elementWeiter = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')
        elementWeiter.click()


if __name__ == "__main__":
    driver = webdriver.Chrome("./chromedriver")
    driver.get("https://www.impfen-saarland.de/service/waitlist_entries")
    loop(driver)