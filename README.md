# automate-python-samples

Documentation for writing Automate test scripts in Python.

Master branch contains **Selenium 3** samples, for **Selenium 4 - W3C protocol** please checkout [selenium-4](https://github.com/browserstack/automate-python-samples/tree/selenium-4) branch


## Environment variables
To test various sample repositories with ease, it is recommended to setup `BROWSERSTACK_USERNAME` and `BROWSERSTACK_ACCESS_KEY` environment variables. Alternatively you can directly update the samples with the credentials or pass the appropriate command line parameters.

## Install Python

### For Windows:

 - Download the latest python build for windows - https://www.python.org/downloads/windows/
 - Run the installer exe and follow the instructions to install python.

### For Mac and Linux:

 - Run python --version to see what python version is installed and make sure it is 3.X and above.
 - Mac OS, Ubuntu and many flavors of linux come with pre-installed python.

## Install Selenium

### For Unix:
```
sudo easy_install selenium
```

### For Windows:
```
easy_install selenium
```

If you prefer pip, then use the following command:
```
sudo pip install selenium
```

If pip is not installed, you can install it using:
```
sudo easy_install pip
```

For Python frameworks samples and integrations with BrowserStack, refer to their individual repositories - 

- [Behave](https://github.com/browserstack/behave-browserstack)
- [Lettuce](https://github.com/browserstack/lettuce-browserstack)
- [Salad](https://github.com/browserstack/salad-browserstack)
