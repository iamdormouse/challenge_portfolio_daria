import os
import time

import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_login_to_the_system(self):          #TC01 passed
        user_login = LoginPage(self.driver)
        dashboard_page = Dashboard(self.driver)
        user_login.do_login()
        dashboard_page.check_logo_visibility()
        time.sleep(3)

    def test_check_login_header(self):           #TC02 failed assertion error
        user_login = LoginPage(self.driver)
        user_login.check_header()
        time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.quit()
