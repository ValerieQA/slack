from selenium import webdriver
from Pages.startPage import LogInPage
from Pages.homePage import PanelMenu
from Pages.signInPage import SignInPage
from Pages.customLoginPage import CustomLoginPage
import unittest
import constants


class SlackTestCases(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        LogInPage(self.driver).opened_log_in_page()

    def tearDown(self):
        self.driver.quit()

    def test_sign_up(self):
        LogInPage(self.driver).click_sign_in()
        SignInPage(self.driver).input_domain()
        CustomLoginPage(self.driver).user_login()

    def test_create_delete_channel(self):
        self.test_sign_up()
        PanelMenu(self.driver).create_channel()
        PanelMenu(self.driver).delete_chanel()

    def test_post_message(self):
        self.test_sign_up()
        PanelMenu(self.driver).post_message()

    def test_set_presence(self):
        self.test_sign_up()
        presence = constants.HomePageConstants.SET_PRESENCE_AWAY
        PanelMenu(self.driver).set_presence(presence)
        presence = constants.HomePageConstants.SET_PRESENCE_ACTIVE
        PanelMenu(self.driver).set_presence(presence)

    def test_set_status(self):
        self.test_sign_up()
        PanelMenu(self.driver).set_status()
        PanelMenu(self.driver).clear_status()


tests = SlackTestCases

if __name__ == "__main__":
    unittest.main()
