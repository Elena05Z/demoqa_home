import unittest
from selenium import webdriver
from pages.swag_labs import SwagLabs


class TestCheckSwag(unittest.TestCase):
    def setUp(self):
        
        self.driver = webdriver.Chrome() 
        self.swag_lab = SwagLabs(self.driver)

    def tearDown(self):
        
        self.driver.quit()

    def test_login_icon_exists(self):
        
        self.swag_lab.visit()
        
        icon_exists = self.swag_lab.exist_icon()
        self.assertTrue(icon_exists, "Иконка страницы входа не обнаружена!")

    def test_username_field_exists(self):
        
        self.swag_lab.visit()
        
        username_field_exists = self.swag_lab.exist_username_field()
        self.assertTrue(username_field_exists, "Поле ввода имени не обнаружено!")

    def test_password_field_exists(self):
        
        self.swag_lab.visit()
        
        password_field_exists = self.swag_lab.exist_password_field()
        self.assertTrue(password_field_exists, "Поле ввода пароля не обнаружено!")


if __name__ == '__main__':
    unittest.main()


from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException


class SwagLabs(BasePage):
    def exist_icon(self):
        try:
           
            self.find_element((By.CSS_SELECTOR, 'div.login_logo'))
            return True
        except NoSuchElementException:
            return False
          

    def exist_username_field(self):
        try:
            
            self.find_element((By.CSS_SELECTOR, '#user-name'))
            return True
        except NoSuchElementException:
            return False

  
    def exist_password_field(self):
        try:
           
            self.find_element((By.CSS_SELECTOR, '#password'))
            return True
        except NoSuchElementException:
            return False
