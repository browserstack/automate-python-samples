from lettuce import *
from lettuce_webdriver.util import assert_false
from lettuce_webdriver.util import AssertContextManager
 
@step('field with name "(.*?)" is given "(.*?)"')
def fill_in_textfield_by_class(step, field_name, value):
    with AssertContextManager(step):
        elem = world.browser.find_element_by_name(field_name)
        elem.send_keys(value)
        elem.submit()

@step(u'Then "([^"]*)" is listed')
def then_result_is_listed(step, result):
    elem = world.browser.find_element_by_xpath("//body[contains(text(), %s)]" %(result))
    assert (not not elem)
