import pytest
import requests
from selenium import webdriver
from modals_page import ModalsPage

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def modals_page(browser):
    return ModalsPage(browser)


def is_page_available(url):
    try:
        resp = requests.head(url)
        if resp.status_code == 200:
            return True
    except requests.RequestException:
        pass
    return False

@pytest.mark.skipif(not is_page_available(ModalsPage.url),
                    reason=f"Страница {ModalsPage.url} недоступна.")
def test_modal_dialogs(modals_page):
    modals_page.open()
    modals_page.click_small_modal_button()
    assert modals_page.check_modal_visible("Small Modal"), "Модал Small Modal не открылся."
    close_btn = modals_page.find_close_button_in_modal()
    close_btn.click()

    modals_page.click_large_modal_button()
    assert modals_page.check_modal_visible("Large Modal"), "Модал Large Modal не открылся."
    close_btn = modals_page.find_close_button_in_modal()
    close_btn.click()
