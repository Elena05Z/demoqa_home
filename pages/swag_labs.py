from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException


class SwagLabs(BasePage):
    def exist_icon(self):
        try:
            self.find_element(locator=(By.CSS_SELECTOR, 'div.login_logo'))
            return True
        except NoSuchElementException:
            return False
