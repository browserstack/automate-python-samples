from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys, json

with open("browsers.json", "r") as f:
    obj = json.loads(f.read())

instance_caps= obj[int(sys.argv[1])]
print "Test "+sys.argv[1]+" started"
# Mention any other capabilities required in the test
caps = {}
caps["browserstack.debug"] = "true"
caps["build"] = "parallel tests"

caps = dict(caps.items() + instance_caps.items())

# THE TEST TO BE RUN PARALLELY GOES HERE

driver = webdriver.Remote(
  command_executor='http://AbhinavSikri:Qxx2dz8Q1sy4qqLYkv71@hub.browserstack.com/wd/hub',
  desired_capabilities=caps)

driver.get("http://www.google.com")
inputElement = driver.find_element_by_name("q")
inputElement.send_keys("browserstack")
inputElement.submit()
print driver.title
driver.quit()