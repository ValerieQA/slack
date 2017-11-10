import constants
import locators


class SignInPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.opened_sign_in_page()

    def opened_sign_in_page(self):
        page_title = self.driver.title
        print page_title
        assert 'Sign in | Slack' in page_title

    def input_domain(self):
        input_domain = self.driver.find_element_by_id(locators.SignInPageLocators.INPUT_DOMAIN)
        input_domain.send_keys(constants.SignInDomainPageConstants.DOMAIN_NAME)
        button_continue = self.driver.find_element_by_id(locators.SignInPageLocators.BUTTON_CONTINUE)
        button_continue.click()
