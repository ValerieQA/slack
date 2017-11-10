from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Waits(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def waitToBeClickable(self, by, identifier):
        self.wait.until(EC.element_to_be_clickable((by, identifier)))

    def waitForTitle(self, title):
        self.wait.until(EC.title_is(title))

    def waitElementNotVisible(self, by, identifier):
        self.wait.until(EC.invisibility_of_element_located((by, identifier)))

    def waitElementVisible(self, by, identifier):
        self.wait.until(EC.visibility_of_element_located((by, identifier)))

    def waitElementPresense(self, by, identifier):
        self.wait.until(EC.presence_of_element_located((by, identifier)))
