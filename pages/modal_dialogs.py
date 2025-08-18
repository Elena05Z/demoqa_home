from selenium.webdriver.common.by import By
from base.page_base import BasePage


   class ModalDialogsPage(BasePage):
       MODAL_BUTTONS = (By.CSS_SELECTOR, ".btn.btn-primary")

       def __init__(self, driver):
           super().__init__(driver)

       def go_to_modal_dialogs(self):
           self.driver.get("https://demoqa.com/modal-dialogs")

       def count_buttons(self):
           return len(self.find_elements(*self.MODAL_BUTTONS))


   HOME_ICON = (By.XPATH, "//img[@alt='ToolsQA']")  

       def click_home_icon(self):
           self.click_element(*self.HOME_ICON)

       def refresh_page(self):
           self.driver.refresh()

       def navigate_back(self):
           self.driver.back()

       def navigate_forward(self):
           self.driver.forward()

       def set_window_size(self, width, height):
           self.driver.set_window_size(width, height)
