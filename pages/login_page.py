 from pages.base_page import BasePage


 class LoginPage(BasePage):
     header_xpath = "//*[text()='Scouts Panel']"
     login_placeholder_xpath = "//*[@id='login-label']"
     login_field_xpath = "//*[@id='login']"
     password_placeholder_xpath = "//*[@id='password-label']"
     password_field_xpath = "//*[@id='password']"
     remind_password_hyperlink_xpath = "//a[text()='Remind password']"
     language_button_xpath = "//*[@role='button']"
     sign_in_button_xpath = "//*[text()='Sign in']"


     def type_in_email(self, email):
         self.field_send_keys(self.login_field_xpath, email)
