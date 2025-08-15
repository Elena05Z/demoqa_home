import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.accordion import Accordion


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()



def test_visible_accordion(browser):
    page = Accordion(browser)
    page.open_page()
    
    assert page.is_element_visible("#section1Content > p"), "Элемент #section1Content > p невидим!"
    page.click_on_section_heading("section1Heading")
    import time
    time.sleep(2)
    assert not page.is_element_visible("#section1Content > p"), "Элемент #section1Content > p всё ещё видим!"


def test_visible_accordion_default(browser):
    page = Accordion(browser)
    page.open_page()
    hidden_elements = [
        "#section2Content > p:nth-child(1)",
        "#section2Content > p:nth-child(2)",
        "#section3Content > p",
    ]
    
    for locator in hidden_elements:
        assert not page.is_element_visible(locator), f"{locator} виден, хотя должен быть скрыт."
