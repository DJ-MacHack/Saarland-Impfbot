import time
from selenium import webdriver
from chromedriver_py import binary_path

class Bot:

    def __init__(self,city,headlessValue):
        self.city = city
        self.options = webdriver.ChromeOptions()
        self.options.set_headless(headless=headlessValue)
        self.options.add_argument('--window-size=1920,1080')
        self.driver = webdriver.Chrome(executable_path=binary_path,chrome_options=self.options)
        self.callWebsite()
        self.chooseCity(self.city)
        self.überprüfeTermine()

    def callWebsite(self):
        baseUrl = "https://www.impfen-saarland.de/service/waitlist_entries"
        self.driver.get(baseUrl)
        time.sleep(0.5)

    def überprüfeTermine(self):
        time.sleep(0.5)
        elementTerminNichtVerfügbar = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/h5')
        time.sleep(0.5)
        if(elementTerminNichtVerfügbar.get_attribute('innerHTML')=="Keine Termine verfügbar. "):
            elementZurück = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div/button')
            elementZurück.click()
            time.sleep(0.5)
            self.chooseCity(self.city)
            time.sleep(0.5)
            self.überprüfeTermine()

        elif(elementTerminNichtVerfügbar.get_attribute('innerHTML')=="Impftermine auswählen"):
            elementTermin = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[1]/div[2]')
            elementTermin.click()
            elementWeiter = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')
            elementWeiter.click()
            time.sleep(0.5)
            if(self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')):
                elementLogin = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')
                elementLogin.click()                         
                time.sleep(0.5)
            else:
                elementZurück = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[1]')
                elementZurück.click()
                

    def chooseCity(self,city):
        if(city == "Saarbrücken"):
            time.sleep(0.5)
            elementSaarbrücken = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[1]/button[1]')
            time.sleep(0.5)
            elementSaarbrücken.click()
            elementWeiter = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')
            time.sleep(0.5)
            elementWeiter.click()
            time.sleep(0.5)
        if(city == "Saarlouis"):
            time.sleep(0.5)
            elementSaarlouis = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[1]/button[2]')
            elementSaarlouis.click()
            elementWeiter = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')
            elementWeiter.click()
            time.sleep(0.5)
        if(city == "Neunkirchen"):
            time.sleep(0.5)
            elementNeunkirchen = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[1]/button[3]')
            elementNeunkirchen.click()
            elementWeiter = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')
            elementWeiter.click()
            time.sleep(0.5)
        if(city == "Lebach"):
            time.sleep(0.5)
            elementLebach = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[1]/button[4]')
            elementLebach.click()
            elementWeiter = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')
            elementWeiter.click()
            time.sleep(0.5)
        if(city == "LebachNacht"):
            time.sleep(0.5)
            elementLebachNacht = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[1]/button[5]')
            elementLebachNacht.click()
            elementWeiter = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')
            elementWeiter.click()
            time.sleep(0.5)
        

