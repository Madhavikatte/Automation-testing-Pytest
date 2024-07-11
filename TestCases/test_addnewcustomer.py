import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from PageObject import Login_page
from PageObject.Addnewcustomer import AddNewCustomer
from PageObject.Login_page import Login
from Utilities.readproperties import ReadConfig
from Utilities.Customlogger import logGen
import string
import random


class Test_003_Addcustomer:
    baseurl = ReadConfig.getApplicationurl()
    Username = ReadConfig.getusername()
    Password = ReadConfig.getpassword()
    # here we created a logger object to call logger class from Customlogger file
    logger = logGen.logger()

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.setusername(self.Username)
        self.lp.setpassword(self.Password)
        self.lp.clicklogin()
        act_title = "Dashboard / nopCommerce administration"
        if act_title == self.driver.title:
            print('Login Successful')
        else:
            print('login unsuccessful')
       # self.driver.close()

        # if act_title=="Dashboard / nopCommerce administration":
        #     assert True
        # else:
        #     assert False

        self.logger.info('**** starting add customer test case *****')
        self.addcust = AddNewCustomer(self.driver)
        self.addcust.clickonCustomermenu()
        self.addcust.clickonCustomersubmenu()

        self.addcust.clickonAddnew()
        self.email = random_generator() + '@gmail.com'
        self.addcust.setEmail(self.email)
        self.addcust.setpassword('test123')
        self.addcust.setFirstname('madhavi')
        self.addcust.setLastname('katte')
        self.addcust.setGender('female')
        self.addcust.setDOB('17/04/2021')
        self.addcust.setCompanyname('test')
        self.addcust.setCustomerRole('Guest')
        self.addcust.click_on_save()

        self.logger.info('saving customer info **')
        self.logger.info('** add customer validation **')
        self.msg = self.driver.find_element(By.TAG_NAME, 'Body').text

        print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            assert True == True
        else:
            self.driver.save_screenshot('Screenshots' + 'addcustomer')
            self.logger.error('** add customer test case failed ***')
            assert True == False
        self.driver.close()
        self.logger.info('** ending add customer test **')


def random_generator(size=8, char=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(char) for x in range(size))
