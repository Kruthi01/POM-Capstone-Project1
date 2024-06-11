from Data import data
from Locator import locator
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

class LoginPage:


   def __init__(self):
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

   def boot(self):
       self.driver.get(data.WebData().url)
       self.driver.maximize_window()
       self.driver.implicitly_wait(10)

   def quit(self):
       self.driver.quit()

   def login(self):
       try:
           self.boot()
           locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
           locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator, data.WebData().password)
           locator.WebLocators().clickButton(self.driver, locator.WebLocators().buttonLocator)
           self.driver.implicitly_wait(10)
           locator.WebLocators().clickButton(self.driver,locator.WebLocators().buttonLocator1)
           self.driver.implicitly_wait(10)
           locator.WebLocators().clickButton(self.driver,locator.WebLocators().addbutton)
           self.driver.implicitly_wait(10)
           locator.WebLocators().enterText(self.driver,locator.WebLocators().fnameLocator,data.WebData().fname)
           locator.WebLocators().enterText(self.driver,locator.WebLocators().lnameLocator,data.WebData().lname)
           locator.WebLocators().clickButton(self.driver,locator.WebLocators().savebuttonLocator)
           locator.WebLocators().enterText(self.driver,locator.WebLocators().otheridLocator,data.WebData().otherid)
           self.driver.implicitly_wait(10)
           locator.WebLocators().clickButton(self.driver,locator.WebLocators().savebutton1Locator)
           self.driver.implicitly_wait(10)
       except NoSuchElementException as e:
           print("Error!")
       finally:
           self.quit()


obj = LoginPage()
obj.login()
