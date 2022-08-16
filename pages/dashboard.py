from pages.base_page import BasePage


class Dashboard(BasePage):
    main_header_xpath = "//*/div[1]/h6"
    home_icon_xpath = "//*[@d='M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z']"
    main_page_block_xpath = "//*[text()='Main page']"
    players_block_xpath = "//*[text()='Players']"
    language_block_xpath = "//*[text()='Polski']"
    sign_out_block_xpath = "//*[text()='Sign out']"
    players_counter_xpath = "//*[text()='Players count']"
    matches_counter_xpath = "//*[text()='Matches count']"
    reports_counter_xpath = "//*[text()='Reports count']"
    events_counter_xpath = "//*[text()='Events count']"
    logo_xpath = "//*[@title='Logo Scouts Panel']"

    pass