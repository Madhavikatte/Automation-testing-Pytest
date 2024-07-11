import pytest
from selenium import webdriver
from PageObject.Login_page import Login
from Utilities.readproperties import ReadConfig
from Utilities.Customlogger import logGen
from Utilities import XL_Utils

class Test_001_login:
    baseurl=ReadConfig.getApplicationurl()
    path = "Test_data/Logindata.xlsx"

    # here we created a logger object to call logger class from Customlogger file
    logger=logGen.logger()

    # in conftest.py file we have created a fixture named as setup that will return driver instance

    def test_login(self,setup):
        self.logger.info('**** Test_002_login****')
        self.logger.info('**** verifying login DDT *****')
        self.driver=setup
        self.driver.get(self.baseurl)
        self.lp=Login(self.driver)
        self.rows=XL_Utils.getRowCount(self.path,'sheet1')
        print('number of rows',self.row)
        # here a empty list variable is created to make array
        List_status=[]

    # read the data from XL-Utils
        for r in range(2,self.rows+1):
            self.user=XL_Utils.readData(self.path,'sheet1',r,1)
            self.password=XL_Utils.readData(self.path,'sheet1',r,2)
            self.exp=XL_Utils.readData(self.path,'sheet1',r,3)

            self.lp.setusername(self.user)
            self.lp.setpassword(self.password)
            self.lp.clicklogin()
            self.time.sleep(5)

        # verify the result using following conditions
            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp=='pass':
                    self.logger.info('*** passed ***')
                    self.lp.clickLogout()
                    List_status.append('pass')
                elif self.exp=='fail':
                    self.logger.info('*** Failed ***')
                    self.lp.clickLogout()
                    List_status.append('fail')
            elif act_title != exp_title:
                if self.exp=='fail':
                    self.logger.info('***passed***')
                    self.lp.clickLogout()
                    List_status.append('pass')
                elif self.exp == 'pass':
                    self.logger.info('***failed***')
                    List_status.append('Fail')

        if 'fail' not in List_status :
            self.logger.info('*** Login DDT test passed')
            self.driver.close()
            assert True
        else:
            self.logger.info('*** Login DDT test failed ***')
            self.driver.close()
            assert False
        self.logger.info('**** end of Login DDT ****')
        self.logger.info('**** Completed TC_login_002 ****')










