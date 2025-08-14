class Component:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, selector):
        return self.driver.find_element(By.CSS_SELECTOR, selector)
    
    def get_text(self):
        element = self.find_element()
        return str(element.text)


from selenium import webdriver
import pytest
from pages.component import Component

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_footer_text(browser):
    component = Component(browser)
    browser.get("https://demoqa.com/")
    footer_text = component.get_text("#footer-copyright")
    expected_text = "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."
    assert footer_text.strip() == expected_text, f"Ожидалось '{expected_text}', получено '{footer_text}'"


def test_elements_page_text(browser):
    component = Component(browser)
    browser.get("https://demoqa.com/")
    elements_button = browser.find_element(By.LINK_TEXT, "Elements")  
    elements_button.click()  
    center_text = component.get_text(".main-header")
    expected_text = "Please select an item from left to start practice."
    assert center_text.strip() == expected_text, f"Ожидалось '{expected_text}', получено '{center_text}'"
