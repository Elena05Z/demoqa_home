import pytest
   from pages.modal_dialogs import ModalDialogsPage


   @pytest.fixture(scope="module")
   def page(driver):
       return ModalDialogsPage(driver)


   def test_modal_elements(page):
       page.go_to_modal_dialogs()
       assert page.count_buttons() == 5, f"Expected 5 buttons but found {page.count_buttons()}."


   def test_navigation_modal(page):
       page.go_to_modal_dialogs()
       page.refresh_page()
       page.click_home_icon()
       current_url = page.driver.current_url
       assert "demoqa.com/" in current_url, f"Current URL is not home page! Current URL: {current_url}"
       
       page.navigate_back()
       page.set_window_size(900, 400)
       page.navigate_forward()
       expected_title = "DEMOQA"
       actual_title = page.driver.title
       assert expected_title in actual_title, f"Title mismatch! Expected '{expected_title}', got '{actual_title}'"

       page.set_window_size(1000, 1000)
