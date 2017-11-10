import constants


class LogInLocators(object):
    SIGN_IN_LINK = "//a[contains(text(), 'Sign in')]"


class SignInPageLocators(object):
    INPUT_DOMAIN = "domain"
    BUTTON_CONTINUE = "submit_team_domain"


class CustomLoginPageLocators(object):
    INPUT_EMAIL = "email"
    INPUT_PASSWORD = "password"
    BUUTON_SIGNIN = "signin_btn"


class HomePageLocators(object):
    NAV_PANEL = "client_channels_list_container"
    BUTTON_ADD_CHANNEL = "p-channel_sidebar__section_heading_plus"
    CREATE_CHANNEL_WIZARD = "public_channel_item"
    INPUT_CHANEL_NAME = "channel_create_title"
    LABEL_CHANNEL_NAME_WARNING = "//span[@class= 'validation_message overflow_ellipsis']"
    BUTTON_CREATE_CHANNEL = "//button[@id = 'save_channel']"
    CREATED_CHANNEL = "//*[@id='col_channels']//span[text()='%s']" % constants.HomePageConstants.CHANNEL_NAME
    CUSTOM_CHANNEL_NAME = "//span[text()='%s']" % constants.HomePageConstants.CHANNEL_NAME
    CHANAL_SELECTED = "channel_title"
    GENERAL_CHANNEL_NAME = "//span[text()='%s']" % constants.HomePageConstants.GENERAL_CHANEL_NAME
    BUTTON_CHANNEL_SETTINGS = "channel_actions_toggle"
    LINK_ADDITIONAL_OPTION = "//li[@id = 'channel_advanced_item']/a[contains(text(), 'Additional options ')]"
    DELETE_CHANNEL = "//div[contains(text(), 'Delete this channel')]"
    CHECKBOX_DELETE_CHANNEL = "//label/input[@id = 'delete_channel_cb']"
    BUTTON_DELETE_CHANNEL = "//button/span[contains(text(), 'Delete Channel')]"
    GENERAL_CHANNEL_SELECTED = "//a[@aria-label='%s (selected, channel)']" % constants.HomePageConstants.GENERAL_CHANEL_NAME
    INPUT_MESSAGE = "//div[@id='msg_input']/div[1]"
    TEXT_POSTED_MESAGE = "//span[text() = '%s']" % constants.HomePageConstants.TEXT_MESSAGE
    USER_NAME = "//*[@id='team_menu_user_details']"
    CURRENT_STATUS = "current_status_input"
    EDITOR_STATUS = "ql-editor"
    COL_CHANNELS = "col_channels"
    CURRENT_PRESENCE = "//span[@class='menu_item_label overflow_ellipsis']/strong"
    SET_PRESENCE = "//span[@class='menu_item_label overflow_ellipsis']/strong[text()='active']"
    ICON_PRESENCE_ACTIVE = "//*[@class='ts_icon ts_icon_presence active']"
    ICON_PRESENCE_AWAY = "//*[@class='ts_icon ts_icon_presence away']"
    EDIT_STATUS = "//*[@id='member_current_status_item']"
    INPUT_STATUS = "//*[@id='current_status_for_team_menu']//div[@class='ql-editor']"
    SET_MESSAGE = "//span[@id='team_menu_user_details']//span[@aria-label='Testing']"
    CLEAR_STATUS = "//a[@aria-label='Clear status']"
