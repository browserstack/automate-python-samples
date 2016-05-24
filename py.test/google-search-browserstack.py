from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Edit these to match your credentials
USERNAME = None
BROWSERSTACK_ACCESS_KEY = None

if not (USERNAME and BROWSERSTACK_ACCESS_KEY):
    raise Exception("Please provide your BrowserStack username and access key")
    sys.exit(1)

def test_run():
    url = "http://%s:%s@hub.browserstack.com/wd/hub" %(
        USERNAME, BROWSERSTACK_ACCESS_KEY
    )

    driver = webdriver.Remote(command_executor=url, desired_capabilities=DesiredCapabilities.FIREFOX)
    driver.get('http://www.google.com')

    if not "Google" in driver.title:
        raise Exception("Are you not on google? How come!")
        elem = driver.find_element_by_name("q")
        elem.send_keys("selenium")
        elem.submit()
        driver.quit()
