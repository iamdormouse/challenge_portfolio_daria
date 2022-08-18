from pages.base_page import BasePage


class LoginPage(BasePage):
    header_xpath = "//h5"
    login_placeholder_xpath = "//*[@id='login-label']"
    login_field_xpath = "//*[@id='login']"
    password_placeholder_xpath = "//*[@id='password-label']"
    password_field_xpath = "//*[@id='password']"
    remind_password_hyperlink_xpath = "//a"
    language_button_xpath = "//input[@value='en' or @value='pl']"
    sign_in_button_xpath = "//*/button[@type='submit']"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
