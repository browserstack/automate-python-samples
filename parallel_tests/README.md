This project contains 3 files. Each of the files is described below.

browsers.json - This file specifies the browser capabilites for the tests. Here, each test would be run in these two browsers. 

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


test.py - This file contains the selenium test which would be run in each of the browsers specificed by "browsers.json". 

    from selenium import webdriver
    import sys, json
    
    json_name = sys.argv[1]
    with open(json_name, "r") as f:
        obj = json.loads(f.read())
    instance_caps= obj[int(sys.argv[2])]
    print "Test "+sys.argv[2]+" started"
    caps = {}
    caps["browserstack.debug"] = "true"
    caps["build"] = "parallel tests" 
    caps = dict(caps.items() + instance_caps.items())
    
    driver = webdriver.Remote(
      command_executor='http://<browserstack_UserName>:<browserstack_AuthKey>@hub.browserstack.com/wd/hub',
      desired_capabilities=caps)
    
    driver.get("http://www.google.com")
    inputElement = driver.find_element_by_name("q")
    inputElement.send_keys("browserstack")
    inputElement.submit()
    print driver.title
    driver.quit()

run_parallel_tests.py - This is the runner which runs the tests in parallel.  

To run the tests in parallel execute the following command:

    python run_parallel_tests.py test.py browsers.json
