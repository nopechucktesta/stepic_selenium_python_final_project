from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_be_no_basket_items(self):
        return self.is_not_element_present(*CartPageLocators.BASKET_ITEMS)

    def should_be_empty_basket_message(self):
        return self.is_element_present(*CartPageLocators.EMPTY_CART_MESSAGE)
