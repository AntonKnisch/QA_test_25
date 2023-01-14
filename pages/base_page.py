
from selenium.webdriver.support.ui import  as wait
from selenium.webdriver.support import expected_conditions as EC




class BasePage:
    def __init__(self, driver , url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locators , timeout=5):
        return wait(self.driver,timeout).until(EC.visibility_of_element_located(locator))
    def element_is_visible(self, locators , timeout=5):
        return wait(self.driver,timeout).until(EC.visibility_of_element_located(locator))
    def element_is_visible(self, locators , timeout=5):
        return wait(self.driver,timeout).until(EC.visibility_of_element_located(locator))
    def element_is_visible(self, locators , timeout=5):
        return wait(self.driver,timeout).until(EC.visibility_of_element_located(locator))
    def element_is_visible(self, locators , timeout=5):
        return wait(self.driver,timeout).until(EC.visibility_of_element_located(locator))