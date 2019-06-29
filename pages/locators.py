from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators(object):
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form .btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "article.product_page .product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "article.product_page .product_main .price_color")
    BASKET_TOTAL_UPDATE_MESSAGE_VALUE = (
        By.XPATH, "//div[@class='alertinner ' and contains(string(), 'Your basket total is now')]//strong")
    HAS_BEEN_ADDED_TO_BASKET_MESSAGE_PRODUCT_NAME = (
        By.XPATH, "//div[@class='alertinner ' and contains(string(), 'has been added to your basket')]/strong")
