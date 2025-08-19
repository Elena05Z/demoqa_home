from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class BasePage:
    def __init__(self, driver, base_url='https://www.saucedemo.com'):
        self.driver = driver
        self.base_url = base_url

    
    def visit(self):
        return self.driver.get(self.base_url)

    
    def find_element(self, locator):
        try:
            return self.driver.find_element(By.CSS_SELECTOR, locator)
        except NoSuchElementException:
            raise Exception(f'Элемент {locator} не найден!')
