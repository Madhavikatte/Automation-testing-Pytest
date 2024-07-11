import time

import pytest
from selenium.webdriver.common.by import By

from PageObject.Login_page import Login
from PageObject.Addnewcustomer import AddNewCustomer
from PageObject.SearchCustomer import searchcustomer
from Utilities.readproperties import ReadConfig
from Utilities.Customlogger import logGen

class Test_005_SearchCustomerBy_name:
    baseurl = ReadConfig.getApplicationurl()
    Username = ReadConfig.getusername()
    Password = ReadConfig.getpassword()
    logger = logGen.logger()

    def test_login(self,setup):
        self.logger.info('*** Login test started ***')
        self.driver= setup
        lp=Login(self.driver)
        self.driver.get(self.baseurl)
        lp.setusername(self.Username)
        lp.setpassword(self.Password)
        lp.clicklogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
        else:
            assert False
            self.logger.info('**** login test completed ****')
            self.addcust = AddNewCustomer(self.driver)
            self.addcust.clickonCustomermenu()
            self.addcust.clickonCustomersubmenu()


            self.logger.info('*** starting search customer by name test case****')
            self.searchcust = searchcustomer(self.driver)
            self.searchcust.setFirstName('John')
            self.searchcust.setLastName('Smith')

            # searchcust.clickonSearch()
            element = self.driver.find_element(By.XPATH, '//*[@id="search-customers"]')
            # self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(5)

            status=searchcust.searchCustomerByName('John Smith')
            assert True == status
            self.logger.info('***Test_005_SearchCustomerBy_name completed***')
            self.driver.close()
