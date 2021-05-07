import requests
from selenium import webdriver
import time
from playsound import playsound

def loop(driver):
    while True:
        findSaarbrücken(driver)
        checkKeineTermine(driver)
        
  
def findSaarbrücken(driver):
    elementSaarbrücken = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[1]/button[1]')
    elementSaarbrücken.click()
    time.sleep(0.3)
    elementWeiter = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')
    elementWeiter.click()
    time.sleep(0.3)

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
    elif(elementTerminNichtVerfügbar.get_attribute('innerHTML')=="Impftermine auswählen"):
        elementTermin = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[1]/div[2]')
        elementTermin.click()
        elementWeiter = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')
        elementWeiter.click()
        time.sleep(0.05)
        if(driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')):
            elementLogin = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')
            elementLogin.click()                         
            time.sleep(0.5)
            elementEmail = driver.find_element_by_xpath('//*[@id="login-form-fields"]/div[1]/input[1]')
            elementEmail.send_keys(input("E-Mail eingeben: "))
            elementCode = driver.find_element_by_xpath('//*[@id="login-form-fields"]/div[3]/input')
        else:
            elementZurück = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[1]')
            elementZurück.click()
            
        


if __name__ == "__main__":
    driver = webdriver.Chrome("./chromedriver")
    driver.get("https://www.impfen-saarland.de/service/waitlist_entries")
    loop(driver)