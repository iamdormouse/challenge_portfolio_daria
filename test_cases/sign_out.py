import os
import time

import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestDashboardPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_check_dashboard_title(self):               #TC03 Failed assertion error
        user_login = LoginPage(self.driver)
        dashboard_page = Dashboard(self.driver)
        user_login.do_login()
        dashboard_page.title_of_page()

    def test_check_dashboard_header(self):              #TC04  Failed
        user_login = LoginPage(self.driver)
        dashboard_page = Dashboard(self.driver)
        user_login.do_login()
        dashboard_page.check_dashboard_header()
        time.sleep(3)

    def test_sign_out_of_system(self):                    #TC07 Sign out of the system  failed
        user_login = LoginPage(self.driver)
        dashboard_page = Dashboard(self.driver)
        user_login.do_login()
        dashboard_page.click_on_the_sign_out_button()
        time.sleep(3)

    def test_switch_the_language(self):                   #TC05 Switch the language  passed
        user_login = LoginPage(self.driver)
        dashboard_page = Dashboard(self.driver)
        user_login.do_login()
        dashboard_page.switch_the_language()
        time.sleep(3)

    def test_logo_visibility(self):                       #TC06 Check Logo visibility
        user_login = LoginPage(self.driver)
        dashboard_page = Dashboard(self.driver)
        user_login.do_login()
        dashboard_page.check_logo_visibility()
        time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.quit()
