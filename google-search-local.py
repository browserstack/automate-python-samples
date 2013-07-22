from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Firefox()
driver.get("http://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")

elem = driver.find_element_by_name("q")
elem.send_keys("selenium")
elem.submit()

print driver.title
driver.quit()
