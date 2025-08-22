from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AlertsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/alerts"
        self.timer_alert_button_id = "#timerAlertButton"

    
    def open(self):
        self.driver.get(self.url)

    
    def click_timer_alert_button(self):
        button = self.driver.find_element(By.CSS_SELECTOR, self.timer_alert_button_id)
        button.click()

    
    def accept_alert(self):
        WebDriverWait(self.driver, 6).until(EC.alert_is_present()).accept()

    
    def verify_alert_appears_after_5_seconds(self):
        start_time = time.time()
        WebDriverWait(self.driver, 6).until(EC.alert_is_present())
        elapsed_time = round(time.time() - start_time)
        return elapsed_time >= 5
