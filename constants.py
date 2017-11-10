import datetime


class StartPageConstants(object):
    URL_START_PAGE = "https://slack.com/"


class SignInDomainPageConstants(object):
    DOMAIN_NAME = "*****"


class CustomLoginPageConstants(object):
    EMAIL = "********@****.***"
    PASSWORD = "*******"


class HomePageConstants(object):
    CHANNEL_NAME = "".join(("s").lower().split())
    CHANNEL_PURPOSE = "TempChannelPurpose"
    GENERAL_CHANEL_NAME = "general"
    TIMESTAMP = str(datetime.datetime.now())
    TEXT_MESSAGE = "Hello World! " + TIMESTAMP
    SET_PRESENCE_ACTIVE = "away"
    SET_PRESENCE_AWAY = "active"
    SET_STATUS_MESSAGE = "Testing"
    CUSTOM_CHANNEL_TITLE = "%s | TestTeam Slack" % CHANNEL_NAME
