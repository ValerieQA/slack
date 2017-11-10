import locators
import constants
from Pages.signInPage import SignInPage


class LogInPage(object):
    def __init__(self, driver):
        self.driver = driver

    def open_log_in_page(self):
        self.driver.get(constants.StartPageConstants.URL_START_PAGE)

    def opened_log_in_page(self):
        self.open_log_in_page()
        print self.driver.title
        assert 'Where work happens | Slack' in self.driver.title

    def click_sign_in(self):
        sign_in_link = self.driver.find_element_by_xpath(locators.LogInLocators.SIGN_IN_LINK)
        sign_in_link.click()
        return SignInPage(self.driver)
