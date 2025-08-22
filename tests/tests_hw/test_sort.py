import pytest
from selenium import webdriver
from web_tables_page import WebTablesPage

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_sort_columns(driver):
    tables_page = WebTablesPage(driver)
    tables_page.open()
    headers = tables_page.get_column_headers()

    for header in headers:
        initial_class = tables_page.get_sorted_class_for_header(header)
        tables_page.sort_by_header(header)
        final_class = tables_page.get_sorted_class_for_header(header)

        assert initial_class != final_class, f"Состояние сортировки не изменилось для заголовка '{header.text}'"
        assert tables_page.check_sorting_state(header), f"Сортировка не сработала для заголовка '{header.text}'"
