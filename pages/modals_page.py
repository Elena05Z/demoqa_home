from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ModalsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/modal-dialogs"

    
    def open(self):
        self.driver.get(self.url)

    
    def click_small_modal_button(self):
        button = self.driver.find_element(By.ID, "showSmallModal")
        button.click()

    
    def click_large_modal_button(self):
       button = self.driver.find_element(By.ID, "showLargeModal")
        button.click()

    
    def find_close_button_in_modal(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//div[@id='exampleModal']/div/div/button[@data-dismiss='modal']")

    
    def check_modal_visible(self, title: str) -> bool:
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".modal-title"))
            )
            return element.text == title
        except:
            return False

