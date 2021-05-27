from selenium import webdriver
from chromedriver_py import binary_path

class Bot:

    def __init__(self,city):
        self.city = city
        self.options = webdriver.ChromeOptions()
        self.options.set_headless(headless=True)
        self.driver = webdriver.Chrome(executable_path= "./chromedriver.exe" or binary_path,chrome_options=self.options)
        self.callWebsite(self.city)

    def callWebsite(self,url):
        self.driver.get(url)

