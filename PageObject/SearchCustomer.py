from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class searchcustomer:
    txtEmail_id='SearchEmail'
    txtFname_id='SearchFirstName'
    txtLname_id='SearchLastName'
    BtnSearch_Xpath='//*[@id="search-customers"]'
    table_Xpath='//*[@id="customers-grid_wrapper"]/div[1]/div/div'
    tableRows_xpath='//*[@id="customers-grid"]/tbody/tr'
    tableColumn_xpath='//*[@id="customers-grid"]/tbody/tr[1]/td'

    def __init__(self,driver):
        self.driver=driver

    def setEmail(self,email):
        self.driver.find_element(By.ID,self.txtEmail_id).send_keys(email)

    def setFirstName(self,FirstName):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID,'SearchFirstName' ))).send_keys(FirstName)

    def setLastName(self,LastName):
        self.driver.find_element(By.ID,self.txtLname_id).send_keys(LastName)

    def clickonSearch(self):
        self.driver.find_element(By.XPATH,self.BtnSearch_Xpath).click()

    def getNumberofRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tableRows_xpath))

    def getnumberofColumn(self):
        return len(self.driver.find_element(By.XPATH,self.tableColumn_xpath))

    # here we are predefining methods to search customer by EMAIL and NAME and we will call the method in test case

    def searchCustomerByEmail(self,email):
        flag=False
        number_of_rows = self.getNumberofRows()
        for r in range(1, number_of_rows + 1):
            Table= self.driver.find_element(By.XPATH,self.table_Xpath)
            email_XPATH= f'//*[@id="customers-grid"]/tbody/tr[{r}]/td[2]'
            email_id=Table.find_element(By.XPATH,email_XPATH).text
            if email_id==email:
                flag=True
                break
        return flag

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.number_of_rows + 1):
            Table = self.driver.find_element(By.XPATH, self.table_Xpath)
            name = Table.find_element(By.XPATH, '//*[@id="customers-grid"]/tbody/tr["+str(r)+"]/td[3]').text
            if name == Name:
                flag = True
                break
        return flag








