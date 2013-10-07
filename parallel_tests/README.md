To run a selenium test on various OS/Browser combinations parallelly:
----------------------------------------------------------------
The maximum number of parallel sessions you can run is inline with the parallel limit on your subscription.

Run from shell "python run_parallel_tests.py < your_test.py > < json_file.py >" 
For the given example test it would be: "python run_parallel_tests.py test.py browsers.json" 

< json_file.json > Add the Browser/OS capabilities required in a json file (like 'browsers.json' in the given example).
eg: For two parallel tests with following capabilities, your json file would look like:

    [
      {
        "browserName": "iPhone",
        "platform": "MAC",
        "device": "iPhone 5"
      },
      {
        "browser": "firefox",
        "browser_version": "17.0",
        "os": "Windows",
        "os_version": "8"
      }
    ]


< your_test.py > should have the format of test.py to run the tests parallelly.
You can mention the extra capabilities required for all tests as mentioned in test.py.
You can add your customized python selenium code as mentioned in test.py.

Do add your own browserstack Username and Access Keys from the Automate dashboard in the test file.

eg : The sample test :
    
    from selenium import webdriver
    import sys, json
    
    json_name = sys.argv[1]
    
    with open(json_name, "r") as f:
        obj = json.loads(f.read())
    
    instance_caps= obj[int(sys.argv[2])]
    print "Test "+sys.argv[2]+" started"
    
    #------------------------------------------------------#
    # Mention any other capabilities required in the test
    caps = {}
    caps["browserstack.debug"] = "true"
    caps["build"] = "parallel tests"
    
    #------------------------------------------------------#
    
    caps = dict(caps.items() + instance_caps.items())
    
    #------------------------------------------------------#
    # THE TEST TO BE RUN PARALLELY GOES HERE
    
    driver = webdriver.Remote(
      command_executor='http://<browserstack_UserName>:<browserstack_AuthKey>@hub.browserstack.com/wd/hub',
      desired_capabilities=caps)
    
    driver.get("http://www.google.com")
    inputElement = driver.find_element_by_name("q")
    inputElement.send_keys("browserstack")
    inputElement.submit()
    print driver.title
    driver.quit()
    #------------------------------------------------------#
