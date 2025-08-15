from selenium.webdriver.common.by import By
from base.base_class import BaseClass


class Accordion(BaseClass):
    SECTION_1_CONTENT_LOCATOR = "#section1Content > p"
    SECTION_1_HEADING_LOCATOR = "#section1Heading"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_page(self):
        """Открывает главную страницу"""
        self.driver.get("https://demoqa.com/accordian")
        
    def is_element_visible(self, locator):
        """
        Возвращает True, если элемент виден, иначе False
        :param locator: CSS селектор элемента
        """
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, locator)
            return element.is_displayed()
        except Exception:
            return False

    def click_on_section_heading(self, heading_id):
        """
        Кликает на указанный заголовок секции
        :param heading_id: ID заголовка секции
        """
        section_heading = self.driver.find_element(By.ID, heading_id)
        section_heading.click()
