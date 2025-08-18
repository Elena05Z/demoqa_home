class Component:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, selector):
        return self.driver.find_element(By.CSS_SELECTOR, selector)
    
    def get_text(self):
        element = self.find_element()
        return str(element.text)
