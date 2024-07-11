from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# create login class
class Login:

    textbox_username_Xpath='//*[@id="Email"]'
    textbox_password_id="Password"
    button_login_Xpath='//*[@id="main"]/div/div/div/div[2]/div[1]/div/form/div[3]/button'
    Link_logout_linktext="Logout"

    def __init__(self,driver):
        self.driver=driver


    def setusername(self,Username):

        #self.driver.find_element(By.XPATH,self.textbox_username_Xpath).clear()

        try:
           element=WebDriverWait(self.driver,10).until(EC.presence_of_element_located(By.CLASS_NAME,self.textbox_username_Class))
           element.send_keys(Username)
        except: NoSuchElementException
        print(f"Username Element not found ")

    def setpassword(self,Password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(Password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH,self.button_login_Xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.Link_logout_linktext).click()