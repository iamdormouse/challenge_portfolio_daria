import os
import time

import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.add_player_page import AddPlayerPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_a_player(self):                          #TC08 Add Player Failed
        user_login = LoginPage(self.driver)
        dashboard_page = Dashboard(self.driver)
        add_player_page = AddPlayerPage(self.driver)
        user_login.do_login()
        dashboard_page.click_add_player()
        add_player_page.type_in_name('Peter')
        add_player_page.type_in_surname('Griffin')
        add_player_page.type_in_age('01.01.1980')
        add_player_page.type_in_main_position('family guy')
        add_player_page.type_in_previous_club('Dolny Slask')
        add_player_page.click_submit_button()
        add_player_page.wait_for_player_to_be_added()
        time.sleep(5)

    def test_clear_the_form(self):                             #TC09 Clear the form
        user_login = LoginPage(self.driver)
        dashboard_page = Dashboard(self.driver)
        add_player_page = AddPlayerPage(self.driver)
        user_login.do_login()
        dashboard_page.click_add_player()
        add_player_page.type_in_name('Peter')
        add_player_page.type_in_surname('Griffin')
        add_player_page.click_clear_button()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()
