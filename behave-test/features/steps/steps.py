@when('visiting google')
def step(context):
    context.browser.get('http://www.google.com')

@then('its title should be "Google"')
def step(context):
    assert context.browser.title == "Google"
