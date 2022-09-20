from lib2to3.pgen2 import driver

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class Dashboard(BasePage):
    main_header_xpath = "//*/div[1]/header/div/h6"
    home_icon_xpath = "//*[@d='M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z']"
    main_page_block_xpath = "//*/ul[1]/div[1]"
    players_block_xpath = "//*/ul[1]/div[2]"
    players_icon_xpath = "//*[contains(@d, '4v2h16v')]"
    language_block_xpath = "//*/ul[2]/div[1]"
    language_icon_xpath = "//*[starts-with(@d, 'M12.87')]"
    sign_out_block_xpath = "//*[text()='Sign out']"
    sign_out_icon_xpath = "//*[starts-with(@d, 'M13')]"
    players_counter_xpath = "//*[text()='Players count']"  #or //main/descendant::div[5]
    number_of_players_xpath = "//*[text()='Players count']/following::b[1]"  #or //main/descendant::div[6]
    matches_counter_xpath = "//*[text()='Matches count']"  #or //main/descendant::div[9]
    number_of_matches_xpath = "//*[text()='Matches count']/following::b[1]"  #or //main/descendant::div10]
    reports_counter_xpath = "//*[text()='Reports count']"  #etc
    number_of_reports_xpath = "//*[text()='Reports count']/following::b[1]"
    events_counter_xpath = "//*[text()='Events count']"
    number_of_events_xpath = "//*[text()='Events count']/following::b[1]"
    logo_xpath = "//*[contains(@style, 'logo')]"
    scouts_panel_xpath = "//h2[text()='Scouts Panel']"
    caption_xpath = "//h2[text()='Scouts Panel']/following::p"
    contact_link_xpath = "//a[@target='_blank']"
    shortcuts_xpath = "//*/div[3]/div[2]/div/div/h2"
    add_player_button_xpath = "//*[@href='/en/players/add']"
    activity_xpath = "//main//div[3]/div/div/h2"
    dashboard_url = 'https://scouts.futbolkolektyw.pl/en/'
    expected_title = 'Scouts panel'
    expected_text = 'Scouts Panel'
    wait = WebDriverWait(driver, 10)

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.add_player_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_the_sign_out_button(self):
        self.wait_for_element_to_be_clickable(self.sign_out_block_xpath)
        self.click_on_the_element(self.sign_out_block_xpath)

    def switch_the_language(self):
        self.wait_for_element_to_be_clickable(self.language_block_xpath)
        self.click_on_the_element(self.language_block_xpath)

    def click_add_player(self):
        self.wait_for_element_to_be_clickable(self.add_player_button_xpath)
        self.click_on_the_element(self.add_player_button_xpath)

    def check_logo_visibility(self):
        self.wait_for_visibility_of_element_located(self.logo_xpath)

    def check_dashboard_header(self):
        self.assert_element_text(self.driver, self.main_header_xpath, self.expected_text)

