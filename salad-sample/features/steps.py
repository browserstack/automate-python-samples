import nose
from salad.steps.everything import *

@step('field with name "(.*?)" is given "(.*?)"')
def fill_in_textfield_by_class(step, field_name, value):
        elem = world.browser.find_element_by_name(field_name)
        elem.send_keys(value)
        elem.submit()

@step(u'Then "([^"]*)" is listed')
def then_result_is_listed(step, result):
    elem = world.browser.find_element_by_xpath("//body[contains(text(), %s)]" %(result))
    assert elem

@step(u'Given I go to "([^"]*)"')
def given_i_go_to_group1(step, group1):
        world.browser.get(group1)
