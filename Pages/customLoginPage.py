import constants
import locators
from Pages.homePage import PanelMenu


class CustomLoginPage(object):
    def __init__(self, driver):
        self.driver = driver

    def opened_custom_login_page(self):
        current_url = self.driver.current_url
        print (current_url)
        custom_domain_name = str((constants.SignInDomainPageConstants.DOMAIN_NAME).lower())
        domain_url = custom_domain_name + ".slack.com"
        assert custom_domain_name in domain_url

    def input_email(self):
        input_email = self.driver.find_element_by_id(locators.CustomLoginPageLocators.INPUT_EMAIL)
        input_email.clear()
        input_email.send_keys(constants.CustomLoginPageConstants.EMAIL)
        current_text = input_email.get_attribute('value')
        assert current_text == constants.CustomLoginPageConstants.EMAIL

    def input_password(self):
        input_password = self.driver.find_element_by_id(locators.CustomLoginPageLocators.INPUT_PASSWORD)
        input_password.clear()
        input_password.send_keys(constants.CustomLoginPageConstants.PASSWORD)

    def user_login(self):
        CustomLoginPage(self.driver).opened_custom_login_page()
        CustomLoginPage(self.driver).input_email()
        CustomLoginPage(self.driver).input_password()
        button_signin = self.driver.find_element_by_id(locators.CustomLoginPageLocators.BUUTON_SIGNIN)
        button_signin.click()
        PanelMenu(self.driver).opened_nav_panel()
