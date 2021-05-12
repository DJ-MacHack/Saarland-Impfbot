import requests
from selenium import webdriver
import time

def loop(driver):
    zeichen = 0
    zeichen = input("Geben Sie ein beliebiges Zeichen ein, wenn Sie sich eingeloggt haben. ")
    if zeichen != 0:
        driver.get("https://www.impfen-saarland.de/service/waitlist_entries")
        time.sleep(0.35)
        while True:
            findSaarbrücken(driver)
            checkKeineTermine(driver)
        
  
def findSaarbrücken(driver):
    elementSaarbrücken = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[1]/button[1]')
    elementSaarbrücken.click()
    elementWeiter = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')
    elementWeiter.click()
    time.sleep(0.35)

def findSaarlouis(driver):
    elementSaarlouis = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[1]/button[2]')
    elementSaarlouis.click()
    elementWeiter = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')
    elementWeiter.click()
    time.sleep(0.35)

def findNeunkirchen(driver):
    elementNeunkirchen = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[1]/button[3]')
    elementNeunkirchen.click()
    elementWeiter = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')
    elementWeiter.click()
    time.sleep(0.35)

def findLebach(driver):
    elementLebach = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[1]/button[4]')
    elementLebach.click()
    elementWeiter = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')
    elementWeiter.click()
    time.sleep(0.35)

def findLebachNacht(driver):
    elementLebachNacht = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[1]/button[5]')
    elementLebachNacht.click()
    elementWeiter = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')
    elementWeiter.click()
    time.sleep(0.35)
    
def checkKeineTermine(driver):
    elementTerminNichtVerfügbar = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/h5')
    time.sleep(0.05)
    if(elementTerminNichtVerfügbar.get_attribute('innerHTML')=="Keine Termine verfügbar. "):
        elementZurück = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div/button')
        elementZurück.click()
        time.sleep(0.35)
    elif(elementTerminNichtVerfügbar.get_attribute('innerHTML')=="Impftermine auswählen"):
        elementTermin = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[1]/div[2]')
        elementTermin.click()
        elementWeiter = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')
        elementWeiter.click()
        time.sleep(0.05)
        if(driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')):
            elementLogin = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')
            elementLogin.click()                         
            time.sleep(0.35)
            #elementEmail = driver.find_element_by_xpath('//*[@id="login-form-fields"]/div[1]/input[1]')
            #elementEmail.send_keys("test@mail.com")
            #elementCode = driver.find_element_by_xpath('//*[@id="login-form-fields"]/div[3]/input')
        else:
            elementZurück = driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[1]')
            elementZurück.click()
            
        


if __name__ == "__main__":
    driver = webdriver.Chrome("C:\\chromedriver.exe")
    driver.get("https://impfen-saarland.de/service/login")
    loop(driver)