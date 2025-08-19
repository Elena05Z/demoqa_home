import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()  
    yield driver
    driver.quit()


def test_select_state_and_city(browser):
    browser.get("https://demoqa.com/automation-practice-form")
    state_dropdown = Select(browser.find_element(By.ID, "state"))
    state_dropdown.select_by_visible_text("California")  
    city_dropdown = Select(browser.find_element(By.ID, "city"))
    city_dropdown.select_by_visible_text("San Francisco") 
