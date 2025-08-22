import pytest
import time
from alerts_page import AlertsPage
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_timer_alert(driver):
    alerts_page = AlertsPage(driver)
    alerts_page.open()
    alerts_page.click_timer_alert_button()
    result = alerts_page.verify_alert_appears_after_5_seconds()
    assert result, "Алерт не появился через ~5 секунд."
    alerts_page.accept_alert()
