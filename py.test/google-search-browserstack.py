import os
import sys

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Edit these to match your credentials
USERNAME = os.environ.get('BROWSERSTACK_USERNAME') or sys.argv[1]
BROWSERSTACK_ACCESS_KEY = os.environ.get(
    'BROWSERSTACK_ACCESS_KEY') or sys.argv[2]

if not (USERNAME and BROWSERSTACK_ACCESS_KEY):
    raise Exception("Please provide your BrowserStack username and access key")


def test_run():
    url = "https://%s:%s@hub.browserstack.com/wd/hub" % (
        USERNAME, BROWSERSTACK_ACCESS_KEY
    )
    capabilities = {
        'browserName': 'Firefox',
        'browserVersion': '65.0',
        'browserstack.use_w3c': 'true',
        'bstack:options': {
            'os': 'Windows',
            'buildName': 'automate-python-samples',
            'osVersion': '10',
            'sessionName': 'unittest_single_test',
            'projectName': 'Sample project',
            'debug': 'true'
        }
    }
    driver = webdriver.Remote(command_executor=url,
                              desired_capabilities=capabilities)
    driver.get('http://www.google.com')

    if not "Google" in driver.title:
        raise Exception("Are you not on google? How come!")
    elem = driver.find_element_by_name("q")
    elem.send_keys("selenium")
    elem.submit()
    driver.quit()
