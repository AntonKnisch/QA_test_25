import time

from locators.elements_page_locaror import TextBoxPageLocators
from pages.base_page import BasePage

class TexBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.SUBMIT_IF_HAVE).click()
        # self.element_is_visible(self.locators.FULL_NAME).send_kys('')
        self.element_is_visible(self.locators.FULL_EMAIL).send_kys('LarryFram.r.10.1.9.93@gmail.com')
        self.element_is_visible(self.locators.FULL_PASSWORD).send_kys('yWGTseV3Qi3dUMZ')
        # self.element_is_visible(self.locators.CURRENT_ADDRESS).send_kys()
        # self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_kys()
        self.element_is_visible(self.locators.SUBMIT).click()
        # self.element_is_visible(self.locators.SUBMIT_IF_ALREADY_HAVE).click()
        time.sleep(5)
