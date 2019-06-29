from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL_INPUT)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_INPUT)
        password_confirm_input = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_CONFIRM_INPUT)
        submit_button = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_SUBMIT_BUTTON)
        email_input.send_keys(email)
        password_input.send_keys(password)
        password_confirm_input.send_keys(password)
        submit_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login page URL is invalid"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"
