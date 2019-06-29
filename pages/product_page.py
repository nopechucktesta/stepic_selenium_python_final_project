from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.add_to_basket_button().click()
        self.solve_quiz_and_get_code()
        product_has_been_added_message = self.wait_for_product_has_been_added_message()
        basket_total_update_message = self.wait_for_basket_total_update_message()
        assert product_has_been_added_message.text == self.product_name(), "Wrong added product name"
        assert basket_total_update_message.text == self.product_price(), "Wrong basket total"

    def add_to_basket_button(self):
        return self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)

    def product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def wait_for_product_has_been_added_message(self):
        return WebDriverWait(self.browser, 5).until(expected_conditions.presence_of_element_located(
            ProductPageLocators.HAS_BEEN_ADDED_TO_BASKET_MESSAGE_PRODUCT_NAME))

    def wait_for_basket_total_update_message(self):
        return WebDriverWait(self.browser, 5).until(expected_conditions.presence_of_element_located(
            ProductPageLocators.BASKET_TOTAL_UPDATE_MESSAGE_VALUE))
