import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()  
    yield driver
    driver.quit()


def test_fill_and_submit_textbox(browser):
    full_name = "Елена Жарова"
    current_address = "Санкт-Петербург, Канонерский остров, д.9"
    browser.get("https://demoqa.com/text-box")
    full_name_input = browser.find_element(By.ID, "userName")
    full_name_input.send_keys(full_name)
    address_input = browser.find_element(By.ID, "currentAddress")
    address_input.send_keys(current_address)
    submit_button = browser.find_element(By.ID, "submit")
    submit_button.click()
    output_fullname = browser.find_element(By.ID, "name").text.strip()
    output_address = browser.find_element(By.ID, "permanentAddress").text.strip()
    
    assert output_fullname.endswith(full_name), f"Ожидалось: '{full_name}', получено: '{output_fullname}'"
    assert output_address.startswith(current_address), f"Ожидалось: '{current_address}', получено: '{output_address}'"
