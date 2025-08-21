from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

def test_case_1():
    driver.get("https://demoqa.com/webtables")
    add_button = wait.until(EC.presence_of_element_located((By.ID, "addNewRecordButton")))
    assert add_button.is_displayed(), "Кнопка Add отсутствует"
    
    add_button.click()
    dialog_window = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-dialog")))
    assert dialog_window.is_displayed(), "Диалоговое окно не открылось"
    
    submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
    submit_button.click()
    error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".rt-tr-group .bg-danger")))
    assert error_message.text.strip() != "", "Ошибка не появилась при попытке отправки пустой формы"
    
    first_name_field = wait.until(EC.visibility_of_element_located((By.ID, "firstName")))
    last_name_field = wait.until(EC.visibility_of_element_located((By.ID, "lastName")))
    email_field = wait.until(EC.visibility_of_element_located((By.ID, "userEmail")))
    age_field = wait.until(EC.visibility_of_element_located((By.ID, "age")))
    salary_field = wait.until(EC.visibility_of_element_located((By.ID, "salary")))
    department_field = wait.until(EC.visibility_of_element_located((By.ID, "department")))
    
    first_name_field.send_keys("TestFirstName")
    last_name_field.send_keys("TestLastName")
    email_field.send_keys("test@example.com")
    age_field.send_keys("30")
    salary_field.send_keys("50000")
    department_field.send_keys("Testing Department")
    
    submit_button.click()
    new_row = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='rt-tbody']//div[contains(text(),'TestFirstName')]")))
    assert new_row.is_displayed(), "Новая запись не была добавлена в таблицу"
    
    edit_icon = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(),'TestFirstName')]/following-sibling::div/button[contains(@title,'Edit')]")))
    edit_icon.click()
    edit_dialog = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-dialog")))
    assert edit_dialog.is_displayed(), "Окно редактирования не открылось"
    
    first_name_field.clear()
    first_name_field.send_keys("UpdatedFirstName")
    submit_button.click()
    updated_row = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='rt-tbody']//div[contains(text(),'UpdatedFirstName')]")))
    assert updated_row.is_displayed(), "Изменения имени не были применены"
    
    delete_icon = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(),'UpdatedFirstName')]/following-sibling::div/button[contains(@title,'Delete')]")))
    delete_icon.click()
    deleted_row = wait.until_not(EC.visibility_of_element_located((By.XPATH, "//div[@class='rt-tbody']//div[contains(text(),'UpdatedFirstName')]")))
    assert not deleted_row, "Запись не была удалена"

if __name__ == "__main__":
    try:
        test_case_1()
        print("Тест-кейс №1 успешно пройден!")
    finally:
        driver.quit()


def test_case_2():
    driver.get("https://demoqa.com/webtables")
    rows_count = len(wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='rowgroup']/div"))))
    assert rows_count == 5, f"Количество строк не соответствует ожидаемому значению {rows_count}"
    
    next_button = wait.until(EC.presence_of_element_located((By.ID, "nextPageBtn")))
    previous_button = wait.until(EC.presence_of_element_located((By.ID, "previousPageBtn")))
    assert "disabled" in next_button.get_attribute("class"), "Кнопка Next доступна изначально"
    assert "disabled" in previous_button.get_attribute("class"), "Кнопка Previous доступна изначально"
    
    for _ in range(3):
        add_button = wait.until(EC.element_to_be_clickable((By.ID, "addNewRecordButton")))
        add_button.click()
        first_name_field = wait.until(EC.visibility_of_element_located((By.ID, "firstName")))
        first_name_field.send_keys(f"User_{_+1}")
        submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
        submit_button.click()
    
    page_info = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "react-paginate")))
    assert "of 2" in page_info.text, "Вторая страница не появилась"
    
    next_button = wait.until(EC.element_to_be_clickable((By.ID, "nextPageBtn")))
    assert "disabled" not in next_button.get_attribute("class"), "Кнопка Next осталась неактивной"
    
    next_button.click()
    second_page_rows = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='rowgroup']/div")))
    assert len(second_page_rows) > 0, "Вторая страница не отображается правильно"
    
    previous_button = wait.until(EC.element_to_be_clickable((By.ID, "previousPageBtn")))
    previous_button.click()
    first_page_rows = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='rowgroup']/div")))
    assert len(first_page_rows) == 5, "Первая страница отображается неправильно"

if __name__ == "__main__":
    try:
        test_case_2()
        print("Тест-кейс №2 успешно пройден!")
    finally:
        driver.quit()


