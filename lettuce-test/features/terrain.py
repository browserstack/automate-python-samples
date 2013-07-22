from lettuce import before, after, world
from selenium import webdriver
import lettuce_webdriver.webdriver

# Edit these to match your credentials
USERNAME = None
BROWSERSTACK_KEY = None

if not (USERNAME and BROWSERSTACK_KEY):
    raise Exception("Please provide your BrowserStack username and access key")
    sys.exit(1)


@before.all
def setup_browser():
    desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
    desired_capabilities['platform'] = 'WINDOWS'

    world.browser = webdriver.Remote(
        desired_capabilities=desired_capabilities,
        command_executor="http://%s:%s@hub.browserstack.com/wd/hub" % (
            USERNAME, BROWSERSTACK_KEY
        )
    )

@after.all
def cleanup_browser(total):
    world.browser.quit()
