from selenium import webdriver

# Edit these to match your credentials
USERNAME = None
BROWSERSTACK_KEY = None

if not (USERNAME and BROWSERSTACK_KEY):
    raise Exception("Please provide your BrowserStack username and access key")
    sys.exit(1)

def before_all(context):
    desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
    desired_capabilities['platform'] = 'WINDOWS'

    context.browser = webdriver.Remote(
        desired_capabilities=desired_capabilities,
        command_executor="http://%s:%s@hub.browserstack.com/wd/hub" % (
            USERNAME, BROWSERSTACK_KEY
        )
    )

    def after_all(context):
        context.browser.quit()
