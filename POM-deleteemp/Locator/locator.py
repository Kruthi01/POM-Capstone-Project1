from selenium.webdriver.common.by import By




class WebLocators:


   def __init__(self):
       self.usernameLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'
       self.passwordLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'
       self.buttonLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
       self.buttonLocator1 = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
       self.addbutton = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
       self.fnameLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input'
       self.lnameLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input'
       self.savebuttonLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
       self.otheridLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input'
       self.savebutton1Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button'
       self.empnameLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input'
       self.searchbuttonLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'
       self.editbuttonLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[2]'
       self.middlenameLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div[2]/div[2]/input'
       self.savebutton2Locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button'
       self.deletebuttonLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[1]'
       self.confirmdeleteLocator = '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]'
   def enterText(self, driver, locator, textValue):
       driver.find_element(by=By.XPATH, value=locator).send_keys(textValue)


   def clickButton(self, driver, locator):
       driver.find_element(by=By.XPATH, value=locator).click()
