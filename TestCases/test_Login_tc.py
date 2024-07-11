import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObject.Login_page import Login
from Utilities.readproperties import ReadConfig
from Utilities.Customlogger import logGen

class Test_001_login:
    baseurl=ReadConfig.getApplicationurl()
    Username=ReadConfig.getusername()
    Password=ReadConfig.getpassword()
    # here we created a logger object to call logger class from Customlogger file
    logger=logGen.logger()

    # in conftest.py file we have created a fixture named as setup that will return driver instance

    def test_homepagetitle(self,setup):
        # we are using the logger object into the test case
        self.logger.info('**** Test_001_login****')
        self.logger.info('**** Verifying Home Page ****')
        self.driver=setup
        self.driver.get (self.baseurl)
        act_title=self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info('**** Home page tittle verification test passed *****')

        else:
            assert False
            self.driver.save_screenshot(".//Screenshots//" + "homepagetitle.png")
            self.driver.close
            self.logger.error('**** Home page tittle verification test failed *****')



    def test_login(self,setup):
        self.driver=setup
        self.driver.get(self.baseurl)
        self.lp=Login(self.driver)
        self.lp.setusername(self.Username)
        self.lp.setpassword(self.Password)
        self.lp.clicklogin()
        act_title= "Dashboard / nopCommerce administration"
        if act_title==self.driver.title:
            print('Login Successful')
        else:
            print('login unsuccessful')




        # # Wait for the title to be "Dashboard / nopCommerce administration"
        # try:
        #     WebDriverWait(self.driver, 10).until(
        #         EC.title_contains("Dashboard / nopCommerce administration")
        #     )
        #     act_title = self.driver.title
        #
        # except Exception as e:
        #     assert act_title == "Dashboard / nopCommerce administration", "Login not successful"
        #
        #
        # self.driver.quit()  # Use quit() to close the entire browser session





