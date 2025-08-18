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
