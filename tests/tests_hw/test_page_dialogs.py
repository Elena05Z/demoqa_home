import pytest
   from pages.modal_dialogs import ModalDialogsPage


   @pytest.fixture(scope="module")
   def page(driver):
       return ModalDialogsPage(driver)


   def test_modal_elements(page):
       page.go_to_modal_dialogs()
       assert page.count_buttons() == 5, f"Expected 5 buttons but found {page.count_buttons()}."
