from selenium import webdriver
from selenium.webdriver.common.by import By
import os, sys, json

try:
    json_name = sys.argv[1]
    counter_val = sys.argv[2]
except IndexError:
    print('Json name and counter val must be passed as first and second argument, respectively, from the comamnd line')
    sys.exit(1)

USERNAME = os.environ.get('BROWSERSTACK_USERNAME') or sys.argv[2]
BROWSERSTACK_ACCESS_KEY = os.environ.get('BROWSERSTACK_ACCESS_KEY') or sys.argv[3]

with open(json_name, "r") as f:
    obj = json.loads(f.read())

instance_caps = obj[int(counter_val)]
print("Test %s started" % (counter_val))

#------------------------------------------------------#
# Mention any other capabilities required in the test
caps = {}
caps["browserstack.debug"] = "true"
caps["build"] = "parallel tests"

#------------------------------------------------------#

caps = {**caps, **instance_caps}

#------------------------------------------------------#
# THE TEST TO BE RUN PARALLELY GOES HERE

driver = webdriver.Remote(
    command_executor='https://%s:%s@hub.browserstack.com/wd/hub' % (
        USERNAME, BROWSERSTACK_ACCESS_KEY
    ),
    desired_capabilities=caps
)

driver.get("http://www.google.com")
inputElement = driver.find_element(By.NAME, "q")
inputElement.send_keys("browserstack")
inputElement.submit()
print(driver.title)
driver.quit()
#------------------------------------------------------#
