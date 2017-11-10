from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import customWaits

import constants
import locators


class PanelMenu(object):
    def __init__(self, driver):
        self.driver = driver

    def opened_nav_panel(self):
        nav_panel = self.driver.find_element_by_class_name(locators.HomePageLocators.NAV_PANEL)
        nav_panel.is_displayed()

    def create_channel(self):
        customWaits.Waits(self.driver).waitToBeClickable(By.CLASS_NAME, locators.HomePageLocators.BUTTON_ADD_CHANNEL)
        create_channel = self.driver.find_element(By.CLASS_NAME, locators.HomePageLocators.BUTTON_ADD_CHANNEL)
        create_channel.click()
        create_channel_wizard_is_opened = self.driver.find_element_by_class_name(
            locators.HomePageLocators.CREATE_CHANNEL_WIZARD)
        create_channel_wizard_is_opened.is_displayed()
        input_wizard_name = self.driver.find_element(By.ID, locators.HomePageLocators.INPUT_CHANEL_NAME)
        input_wizard_name.send_keys(constants.HomePageConstants.CHANNEL_NAME)
        # wait for validation warning label is not displayed
        customWaits.Waits(self.driver).waitElementNotVisible(By.XPATH,
                                                             locators.HomePageLocators.LABEL_CHANNEL_NAME_WARNING)
        button_create_channel = self.driver.find_element(By.XPATH, locators.HomePageLocators.BUTTON_CREATE_CHANNEL)
        button_create_channel.click()
        customWaits.Waits(self.driver).waitToBeClickable(By.ID, locators.HomePageLocators.COL_CHANNELS)
        customWaits.Waits(self.driver).waitToBeClickable(By.XPATH, locators.HomePageLocators.CREATED_CHANNEL)
        custom_channel = self.driver.find_element(By.XPATH, locators.HomePageLocators.CREATED_CHANNEL)
        custom_channel.is_displayed()

    def delete_chanel(self):
        customWaits.Waits(self.driver).waitToBeClickable(By.XPATH, locators.HomePageLocators.CREATED_CHANNEL)
        custom_channel = self.driver.find_element(By.ID, locators.HomePageLocators.COL_CHANNELS).find_element(By.XPATH,
                                                                                                              locators.HomePageLocators.CUSTOM_CHANNEL_NAME)
        custom_channel.click()
        customWaits.Waits(self.driver).waitForTitle(constants.HomePageConstants.CUSTOM_CHANNEL_TITLE)
        customWaits.Waits(self.driver).waitToBeClickable(By.ID, locators.HomePageLocators.BUTTON_CHANNEL_SETTINGS)
        button_channel_settings = self.driver.find_element(By.ID, locators.HomePageLocators.BUTTON_CHANNEL_SETTINGS)
        button_channel_settings.click()
        link_additional_optional = self.driver.find_element(By.XPATH, locators.HomePageLocators.LINK_ADDITIONAL_OPTION)
        link_additional_optional.click()
        customWaits.Waits(self.driver).waitToBeClickable(By.XPATH, locators.HomePageLocators.DELETE_CHANNEL)
        delete_channel = self.driver.find_element(By.XPATH, locators.HomePageLocators.DELETE_CHANNEL)
        delete_channel.click()
        customWaits.Waits(self.driver).waitToBeClickable(By.XPATH, locators.HomePageLocators.CHECKBOX_DELETE_CHANNEL)
        checkbox_delete_channel = self.driver.find_element(By.XPATH, locators.HomePageLocators.CHECKBOX_DELETE_CHANNEL)
        checkbox_delete_channel.click()
        # verify checkbox
        button_delete_channel = self.driver.find_element(By.XPATH, locators.HomePageLocators.BUTTON_DELETE_CHANNEL)
        button_delete_channel.click()
        self.opened_nav_panel()

    def post_message(self):
        custom_channel = self.driver.find_element(By.ID, locators.HomePageLocators.COL_CHANNELS).find_element(By.XPATH,
                                                                                                              locators.HomePageLocators.GENERAL_CHANNEL_NAME)
        custom_channel.click()
        self.driver.find_element(By.XPATH, locators.HomePageLocators.GENERAL_CHANNEL_SELECTED)
        input_message = self.driver.find_element(By.XPATH, locators.HomePageLocators.INPUT_MESSAGE)
        input_message.send_keys(constants.HomePageConstants.TEXT_MESSAGE)
        input_message.send_keys(Keys.RETURN)
        # message is posted
        posted_message = self.driver.find_element(By.XPATH, locators.HomePageLocators.TEXT_POSTED_MESAGE)
        posted_message_text = posted_message.text
        assert posted_message_text == constants.HomePageConstants.TEXT_MESSAGE

    def set_presence(self, presence_state):
        icon_state = {"away": locators.HomePageLocators.ICON_PRESENCE_ACTIVE,
                      "active": locators.HomePageLocators.ICON_PRESENCE_AWAY}
        customWaits.Waits(self.driver).waitToBeClickable(By.XPATH, locators.HomePageLocators.USER_NAME)
        user_name = self.driver.find_element(By.XPATH, locators.HomePageLocators.USER_NAME)
        user_name.click()
        current_state = self.driver.find_element(By.XPATH, locators.HomePageLocators.CURRENT_PRESENCE).text
        if current_state != presence_state:
            self.driver.find_element(By.XPATH, locators.HomePageLocators.CURRENT_PRESENCE).click()
            get_icon_locator = icon_state.get(presence_state)
            # verify that presence is set
            customWaits.Waits(self.driver).waitElementVisible(By.XPATH, get_icon_locator)
            self.driver.find_element(By.XPATH, get_icon_locator)
        else:
            print "I am not %s" % presence_state

    def open_status_fiels(self):
        customWaits.Waits(self.driver).waitToBeClickable(By.XPATH, locators.HomePageLocators.USER_NAME)
        user_name = self.driver.find_element(By.XPATH, locators.HomePageLocators.USER_NAME)
        user_name.click()
        edit_status = self.driver.find_element(By.XPATH, locators.HomePageLocators.EDIT_STATUS)
        edit_status.click()

    def set_status(self):
        self.open_status_fiels()
        self.driver.find_element_by_xpath(locators.HomePageLocators.EDIT_STATUS).click()
        input_status = self.driver.find_element(By.CLASS_NAME, locators.HomePageLocators.CURRENT_STATUS).find_element(
            By.CLASS_NAME, locators.HomePageLocators.EDITOR_STATUS)
        input_status.clear()
        input_status.send_keys(constants.HomePageConstants.SET_STATUS_MESSAGE)
        input_status.send_keys(Keys.RETURN)
        customWaits.Waits(self.driver).waitElementPresense(By.XPATH, locators.HomePageLocators.SET_MESSAGE)

    def clear_status(self):
        self.open_status_fiels()
        clear_status = self.driver.find_element(By.XPATH, locators.HomePageLocators.CLEAR_STATUS)
        clear_status.click()
        customWaits.Waits(self.driver).waitElementPresense(By.XPATH, locators.HomePageLocators.SET_MESSAGE)
