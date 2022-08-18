from pages.base_page import BasePage


class Dashboard(BasePage):
    main_header_xpath = "//h6[text()='Scouts Panel']"
    home_icon_xpath = "//*[@d='M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z']"
    main_page_block_xpath = "//*[text()='Main page']"  #or //ul[1]/div[1]/span/preceding::span[1]
    players_block_xpath = "//*[text()='Players']"
    players_icon_xpath = "//*[contains(@d, '4v2h16v')]"  #I just added this one after sending my work
    language_block_xpath = "//*[text()='Polski']"
    language_icon_xpath = "//*[starts-with(@d, 'M12.87')]"  #I just added this one after sending my work
    sign_out_block_xpath = "//*[text()='Sign out']"
    sign_out_icon_xpath = "//*[starts-with(@d, 'M13')]"  #I just added this one after sending my work
    players_counter_xpath = "//*[text()='Players count']"
    number_of_players_xpath = "//*[text()='Players count']/following::b[1]"  #I just added this after sending my work
    matches_counter_xpath = "//*[text()='Matches count']"
    number_of_matches_xpath = "//*[text()='Matches count']/following::b[1]"
    reports_counter_xpath = "//*[text()='Reports count']"
    number_of_reports_xpath = "//*[text()='Reports count']/following::b[1]"
    events_counter_xpath = "//*[text()='Events count']"
    number_of_events_xpath = "//*[text()='Events count']/following::b[1]"
    logo_xpath = "//*[@title='Logo Scouts Panel']"
    scouts_panel_xpath = "//h2[text()='Scouts Panel']"
    caption_xpath = "//h2[text()='Scouts Panel']/following::p"
