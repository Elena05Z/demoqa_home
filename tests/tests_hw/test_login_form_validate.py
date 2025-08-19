import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()  
    yield driver
    driver.quit()


def test_automation_practice_form_validation(browser):
    browser.get("https://demoqa.com/automation-practice-form")
    first_name_placeholder = browser.find_element(By.ID, "firstName").get_attribute("placeholder")
    assert first_name_placeholder == "First Name", "Placeholder для First Name неверный."
    
    last_name_placeholder = browser.find_element(By.ID, "lastName").get_attribute("placeholder")
    assert last_name_placeholder == "Last Name", "Placeholder для Last Name неверный."
    
    email_pattern = browser.find_element(By.ID, "userEmail").get_attribute("pattern")
    assert email_pattern == "^([a-zA-Z0-9_\\-\\.]+)@([a-zA-Z0-9_\\-\\.]+)\\.([a-zA-Z]{2,5})$", \\
    "Атрибут pattern для Email некорректен."
    
    form = browser.find_element(By.CLASS_NAME, "practice-form-wrapper")
    submit_button = browser.find_element(By.ID, "submit")
    submit_button.click()
    
    class_list = form.get_attribute("class")
    assert "was-validated" in class_list, "Форма не была валидирована после отправки."
