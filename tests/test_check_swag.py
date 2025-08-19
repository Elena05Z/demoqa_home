from pages.swag_labs import SwagLabs
import pytest


@pytest.fixture(scope="module")
def browser():
    pass


def test_check_icon(browser):
    page = SwagLabs(browser)
    page.visit()
    assert page.exist_icon(), "Иконка отсутствует!"


def test_check_username_field(browser):
    page = SwagLabs(browser)
    page.visit()
    assert page.exist_username_field(), "Поле ввода имени пользователя отсутствует!"


def test_check_password_field(browser):
    page = SwagLabs(browser)
    page.visit()
    assert page.exist_password_field(), "Поле ввода пароля отсутствует!"
