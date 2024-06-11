from selenium.webdriver.common.by import By




class WebLocators:


   def __init__(self):
       self.usernameLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'
       self.passwordLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'
       self.buttonLocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'


   def enterText(self, driver, locator, textValue):
       driver.find_element(by=By.XPATH, value=locator).send_keys(textValue)


   def clickButton(self, driver, locator):
       driver.find_element(by=By.XPATH, value=locator).click()
