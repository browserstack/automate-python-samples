#from lettuce import before, after, world
from selenium import webdriver
#import lettuce_webdriver.webdriver
from salad.terrains.everything import *
# Edit these to match your credentials
USERNAME = "<browserstack-username>"
BROWSERSTACK_KEY = "<browserstack-key>"

if not (USERNAME and BROWSERSTACK_KEY):
    raise Exception("Please provide your BrowserStack username and access key")
    sys.exit(1)


@before.all
def setup_browser():
    desired_capabilities = webdriver.DesiredCapabilities.CHROME
    desired_capabilities['platform'] = 'WINDOWS'
    desired_capabilities['browser'] = 'chrome'
    world.browser = webdriver.Remote(
        desired_capabilities=desired_capabilities,
        command_executor="http://%s:%s@hub.browserstack.com/wd/hub" % (
            USERNAME, BROWSERSTACK_KEY
        )
    )

@after.all
def cleanup_browser(total):
    world.browser.quit()
