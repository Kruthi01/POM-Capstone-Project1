from Data import data
from Locator import locator

from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest
class Test:


   @pytest.fixture
   def boot(self):
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       yield
       self.driver.quit()
   @pytest.mark.html
   def testTitle(self, boot):
       self.driver.get(data.WebData().url)
       assert self.driver.title == data.WebData().loginPageTitle
       print("SUCCESS: Web Title Verified")
   @pytest.mark.html
   def testLogin(self, boot):
       self.driver.get(data.WebData().url)
       self.driver.implicitly_wait(10)
       locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
       locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator, data.WebData().password)
       locator.WebLocators().clickButton(self.driver, locator.WebLocators().buttonLocator)
       self.driver.implicitly_wait(10)
       locator.WebLocators().clickButton(self.driver,locator.WebLocators().buttonLocator1)
       self.driver.implicitly_wait(10)
       locator.WebLocators().clickButton(self.driver,locator.WebLocators().addbutton)
       locator.WebLocators().enterText(self.driver,locator.WebLocators().fnameLocator,data.WebData().fname)
       locator.WebLocators().enterText(self.driver,locator.WebLocators().lnameLocator,data.WebData().lname)
       self.driver.implicitly_wait(10)
       locator.WebLocators().clickButton(self.driver,locator.WebLocators().savebuttonLocator)
       self.driver.implicitly_wait(10)
       locator.WebLocators().enterText(self.driver,locator.WebLocators().otheridLocator,data.WebData().otherid)
       self.driver.implicitly_wait(10)
       locator.WebLocators().clickButton(self.driver,locator.WebLocators().savebutton1Locator)
       self.driver.implicitly_wait(10)

