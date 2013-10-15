"""
@param USERNAME: Browserstack username
@type USERNAME: string
@param BROWSERSTACK_KEY: Browserstack api key
@type BROWSERSTACK_KEY: string
@description: Supply these arguments from commandline while running this script
"""
import sys
import base64
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.webdriver import WebDriver

# Input capabilities
caps = {}
caps["browser"] = "Firefox"
caps["browser_version"] = "24.0"
caps["os"] = "OS X"
caps["os_version"] = "Snow Leopard"
caps["browserstack.debug"] = "true"

# Take input of user credentials
try:
    USERNAME = sys.argv[1]
    BROWSERSTACK_KEY = sys.argv[2]
except IndexError:
    print("Pleaes provide the username, browserstack access key and filename with which screenshot should be saved as command line arguments.")
    sys.exit(1)

# Define take_screenshot 
def take_screenshot(webdriver, file_name = "sample.png"):
    """
    @param webdriver: WebDriver handler.
    @type webdriver: WebDriver
    @param file_name: Name to label this screenshot.
    @type file_name: str 
    """
    if isinstance(webdriver, WebDriver):
        base64_data = webdriver.get_screenshot_as_base64()
        screenshot_data = base64.decodestring(base64_data)
        screenshot_file = open(file_name, "w")
        screenshot_file.write(screenshot_data)
        screenshot_file.close()
    else:
        webdriver.save_screenshot(filename)

driver = webdriver.Remote(
    command_executor = 'http://akshaybhardwaj1:XQWDewaJsUzqYJRv8zhr@hub.browserstack.com/wd/hub',
    desired_capabilities = caps)

driver.get("http://www.google.com")
inputElement = driver.find_element_by_name("q")
inputElement.send_keys("browserstack")
inputElement.submit()
print driver.title
take_screenshot(driver, './sample.png')
driver.quit()
