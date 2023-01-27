import time
from pages.elements_page import TextBoxPage

class TestElements:
    class TestTextBox:
        def test_text_box(self , driver):
            text_box_page = TextBoxPage(driver, 'https://petfriends.skillfactory.ru/login')
            text_box_page.open()
            # text_box_page.SUBMIT_IF_HAVE.click()
            text_box_page.fill_all_fields()
            time.sleep(5)

        def test_my_pets(self, driver):
            my_pets = TextBoxPage (driver , 'https://petfriends.skillfactory.ru/my_pets')
            my_pets.open()
            my_pets.go_to_my_pets()
            time.sleep(5)

# def test(driver):
#     page = BasePage(driver,'https://petfriends.skillfactory.ru/login')
#     page.open()
#     time.sleep(3)