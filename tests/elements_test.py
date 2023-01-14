import time

from pages.base_page import BasePage


def test(driver):
    page = BasePage(driver,'https://petfriends.skillfactory.ru/my_pets')
    page.open()
    time.sleep(3)