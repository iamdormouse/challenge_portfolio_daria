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
    expected_title = 'Scouts panel - sign in'
    login_url = 'https://scouts-test.futbolkolektyw.pl/en/'
    expected_text = 'Scouts Panel'

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def check_header(self):
        self.assert_element_text(self.driver, self.header_xpath, self.expected_text)
