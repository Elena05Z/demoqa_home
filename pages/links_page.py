from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LinksPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/links"
        self.home_link_xpath = '//a[contains(text(),"Home")]'

    
    def open(self):
        self.driver.get(self.url)

    
    def get_home_link(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.home_link_xpath))
        )

    
    def click_home_link(self):
        link = self.get_home_link()
        link.click()

    
    def get_current_windows(self):
        return self.driver.window_handles
