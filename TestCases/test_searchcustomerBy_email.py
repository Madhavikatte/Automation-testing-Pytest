import pytest
from selenium.common import NoSuchElementException

from PageObject.Login_page import Login
from PageObject.Addnewcustomer import AddNewCustomer
from PageObject.SearchCustomer import searchcustomer
from Utilities.readproperties import ReadConfig
from Utilities.Customlogger import logGen

class Test_searchCustomer_By_Email_004:
    baseurl=ReadConfig.getApplicationurl()
    Username=ReadConfig.getusername()
    Password=ReadConfig.getpassword()
    logger=logGen.logger()

    def test_searchCustomerby_email(self,setup):
        self.logger.info('***** Login test started *****')
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp=Login(self.driver)
        self.lp.setusername(self.Username)
        self.lp.setpassword(self.Password)
        self.lp.clicklogin()
        self.logger.info('********** Login Successfull **********')

        self.logger.info('********* Starting customer by email *********')

        self.addcust=AddNewCustomer(self.driver)
        self.addcust.clickonCustomermenu()
        self.addcust.clickonCustomersubmenu()
        self.logger.info('********* searching customer by email *********')

        self.searchcust=searchcustomer(self.driver)
        self.searchcust.setEmail('admin@yourStore.com')
        self.searchcust.clickonSearch()

        status= self.searchcust.searchCustomerByEmail('admin@yourStore.com')
        assert True== status
        print(status)
        self.logger.info('**** TC_004_searchcustomerByEmail_completed ****')
        self.driver.close()











