from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebTablePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/webtables"
        self.header_css_selector = ".rt-thead.-header .rt-tr-group th"

    
    def open(self):
        self.driver.get(self.url)

    
    def get_headers(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.header_css_selector)

    
    def click_on_header(self, header):
        header.click()

    
    def get_sort_order_class(self, header):
        classes = header.get_attribute("class").split()
        return next((cls for cls in classes if cls.startswith("rt-sortable-header--")), None)

    
    def wait_until_sorted(self, header):
        old_class = self.get_sort_order_class(header)
        WebDriverWait(self.driver, timeout=5).until(
            lambda drv: self.get_sort_order_class(header) != old_class,
            message="Смена класса сортировки не произошла"
