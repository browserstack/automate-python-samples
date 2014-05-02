Feature: Go to google
    Scenario: Visit Google
        Given I go to "http://www.google.com/"
            When field with name "q" is given "selenium"
            Then "seleniumhq.org" is listed
