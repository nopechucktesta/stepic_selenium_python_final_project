from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators(object):
    PRODUCT_NAME = (By.CSS_SELECTOR, "article.product_page .product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "article.product_page .product_main .price_color")
