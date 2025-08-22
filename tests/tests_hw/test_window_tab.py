import pytest
from links_page import LinksPage
from selenium import webdriver


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_open_home_link_in_new_tab(driver):
    links_page = LinksPage(driver)
    links_page.open()
    initial_windows = links_page.get_current_windows()
    main_window = driver.current_window_handle
    links_page.click_home_link()
    new_windows = links_page.get_current_windows()
    assert len(initial_windows) + 1 == len(new_windows), "Новая вкладка не появилась"

    new_window = next(w for w in new_windows if w != main_window)
    driver.switch_to.window(new_window)
    actual_url = driver.current_url
    expected_url = "https://demoqa.com/"
    assert actual_url == expected_url, f"URL открытой вкладки отличается ({expected_url}, {actual_url})"

    driver.close()
    driver.switch_to.window(main_window)
