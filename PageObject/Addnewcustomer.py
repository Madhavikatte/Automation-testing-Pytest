import time

from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddNewCustomer :

    lnkcustomer_menu_xpath='/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a'
    lnkcustomer_submenu_xpath='/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a'
    btnaddnew_xpath='/html/body/div[3]/div[1]/form[1]/div/div/a'
    txtemail_xpath='//*[@id="Email"]'
    txtpassword_xpath='//*[@id="Password"]'
    txtfirstname_xpath='//*[@id="FirstName"]'
    txtlastname_xpath='//*[@id="LastName"]'
    Rdmale_gender_id='Gender_Male'
    Rd_female_id='Gender_Female'
    txtDob_xpath='//*[@id="DateOfBirth"]'
    txtcompanyname_xpath='//*[@id="Company"]'
    txtCustomerrole_xpath='//*[@id="customer-info"]/div[2]/div[10]/div[2]/div/div[1]/div/span/span[1]/span/ul'
    lstitemAdminstrator_xpath='//*[@id="select2-SelectedCustomerRoleIds-result-koft-1"]'
    lstitemRegistered_xpath='//*[@id="select2-SelectedCustomerRoleIds-result-5nya-3"]'
    lstitemGuest_xpath='//*[@id="select2-SelectedCustomerRoleIds-result-9647-4"]'
    lstitemVendor_xpath='//*[@id="select2-SelectedCustomerRoleIds-result-6788-5"]'
    drpmgrofvendor_xpath='//*[@id="VendorId"]'
    txtadmincomment='//*[@id="AdminComment"]'
    btnsave_xpath='/html/body/div[3]/div[1]/form/div[1]/div/button[1]'



    def __init__(self,driver):
        self.btnsave_Xpath = None
        self.driver=driver

    def clickonCustomermenu(self):

        try:
          Menu=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.lnkcustomer_menu_xpath)))
          Menu.click()
        except:
            print("Customer menu Element not Found")

    def clickonCustomersubmenu(self):
        try:
            Submenu=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.lnkcustomer_submenu_xpath)))
            Submenu.click()
        except:
            print(" submenu element not found")
            self.driver.get ("https://admin-demo.nopcommerce.com/Admin/Customer/List")



    def clickonAddnew(self):
        self.driver.find_element(By.XPATH,self.btnaddnew_xpath).click()
    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtemail_xpath).send_keys(email)
    def setpassword(self,password):
        self.driver.find_element(By.XPATH,self.txtpassword_xpath).send_keys(password)
    def setFirstname(self,FirstName):
        self.driver.find_element(By.XPATH,self.txtfirstname_xpath).send_keys(FirstName)
    def setLastname(self,Lastname):
        self.driver.find_element(By.XPATH,self.txtlastname_xpath).send_keys(Lastname)
    def setGender(self,gender):
        if gender=='male':
            self.driver.find_element(By.XPATH,self.Rdmale_gender_id).click()
        elif gender=='female':
            self.driver.find_element(By.ID, self.Rd_female_id).click()
        else:
            self.driver.find_element(By.ID,self.Rdmale_gender_id).click()
    def setDOB(self,DOB):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(DOB)
    def setCompanyname(self,CompanyName):
        self.driver.find_element(By.XPATH, self.txtcompanyname_xpath).send_keys(CompanyName)
    def setCustomerRole(self,role):

        self.driver.find_element(By.XPATH, self.txtCustomerrole_xpath).click()
        time.sleep(3)
        ListItem = None  # Define ListItem with None initially
        if role=='Administrator':
            ListItem = self.driver.find_element(By.XPATH, self.lstitemAdminstrator_xpath)
        elif role=='Registered':
            ListItem=self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role=='Guest':
            Registered_remove_xpath = '//*[@id="customer-info"]/div[2]/div[10]/div[2]/div/div[1]/div/span/span[1]/span/ul/li[1]/span'
            try:
                Remove_registered = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(By.XPATH,Registered_remove_xpath))
                Remove_registered.click()

                ListItem = WebDriverWait(self.driver,10,poll_frequency=2).until(EC.presence_of_element_located((By.XPATH, self.lstitemGuest_xpath)))
            except:TimeoutException
            print("Timeout waiting for elements.")

        elif role=='Vendor':
            ListItem = self.driver.find_element(By.XPATH, self.lstitemVendor_xpath)
        else:
            # Handle unknown roles or default case
            raise Exception(f"Role '{role}' is not recognized.")
        if ListItem:
            ListItem.click()
        else:
            print("Role has not selected")

                #the click() action is not working here so we are going to use javascript argument
            # self.driver.execute_script("arguments[0].click();",self.ListItem)

    def click_on_save(self):
        self.driver.find_element(By.XPATH,self.btnsave_xpath).click()
        # try:
        #     save_button = WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located((By.XPATH, self.btnsave_xapth)))
        #     save_button.click()
        # except NoSuchElementException:
        #     print(f"Element not found for xpath: {self.btnsave_Xpath}")
        # except TimeoutException:
        #     print(f"Timeout waiting for element: {self.btnsave_Xpath}")















