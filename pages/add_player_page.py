from pages.base_page import BasePage


class AddPlayerPage(BasePage):
    name_field_xpath = "//*[@name='name']"
    surname_field_xpath = "//*[@name='surname']"
    age_field_xpath = "//*[@name='age']"
    main_position_field_xpath = "//*[@name='mainPosition']"
    submit_button_xpath = "//*[@type='submit']"
    add_player_page_url = 'https://scouts.futbolkolektyw.pl/en/players/add'
    clear_button_xpath = "//*[text()='Clear']"
    added_player_xpath = "//*[text()='Peter Griffin']"
    previous_club_field_xpath = "//*/div[1]/main/div[2]/form/div[2]/div/div[18]/div/div/input"


    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_age(self, age):
        self.field_send_keys(self.age_field_xpath, age)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_field_xpath, main_position)

    def type_in_previous_club(self, previous_club):
        self.field_send_keys(self.previous_club_field_xpath, previous_club)

    def click_submit_button(self):
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
        self.click_on_the_element(self.submit_button_xpath)

    def click_clear_button(self):
        self.wait_for_element_to_be_clickable(self.clear_button_xpath)
        self.click_on_the_element(self.clear_button_xpath)

    def wait_for_player_to_be_added(self):
        self.wait_for_visibility_of_element_located(self.added_player_xpath)
