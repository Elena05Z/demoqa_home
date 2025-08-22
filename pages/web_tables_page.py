from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebTablesPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/webtables"
        self.table_headers_selector = ".rt-th.rt-resizable-header"

    
    def open(self):
        self.driver.get(self.url)

    
    def get_column_headers(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.table_headers_selector)

    
    def sort_by_header(self, column_header):
        column_header.click()

    
    def get_sorted_class_for_header(self, column_header):
        return column_header.get_attribute("class").split()[-1]

    
    def check_sorting_state(self, column_header):
        sorted_class = self.get_sorted_class_for_header(column_header)
        return "sort-desc" in sorted_class or "sort-asc" in sorted_class
