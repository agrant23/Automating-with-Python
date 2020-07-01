#Test_Password_Count

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import random
import string
import time

class Test_Password_Count(unittest.TestCase):                  

    def setUp(self):
        path_to_extension = r'C:\Webdrivers.Extensions\3.8.4_0'
        options = Options() 
        options.add_argument('load-extension=' + path_to_extension)

        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://www.yahoo.com")
        self.driver.create_options()
        
        wait = WebDriverWait(self.driver, 10) 
        
        yahoo_tab = self.driver.current_window_handle
        wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(yahoo_tab)

        sign_in_button = self.driver.find_element_by_id("header-signin-link")
        sign_in_button.click()

        wait.until(EC.url_changes('https://login.yahoo.com/config/login'))              #this succeeded in getting rid of a time.sleep() but below this didn't work
        
        username_field = self.driver.find_element_by_id('login-username')
        
        username_field.send_keys("tonyg1239411@yahoo.com") 

        next_button_loc = (By.XPATH,'//input[@id="login-signin"]')
        next_button1 = self.driver.find_element(*next_button_loc)
        next_button1 = WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable(next_button_loc))
        next_button1.click()
        
        wait.until(EC.url_changes('https://login.yahoo.com/account/challenge/password'))
        time.sleep(2)                                                                       #I really tried to get rid of this time.sleep(2)

        password_field_loc = (By.XPATH,'//input[@id="login-passwd"]')
        password_field = self.driver.find_element(*password_field_loc)
        password_field = WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(password_field_loc))   

        password_field.send_keys("orange23$")
        
        next_button2 = self.driver.find_element_by_xpath('//button[@id="login-signin"]')
        next_button2.click()

        time.sleep(3)                                               #this is needed for the pop up?
        current_tab = self.driver.current_window_handle                  
        self.driver.switch_to.window(current_tab)
        
        current_tab = self.driver.current_window_handle                  
        self.driver.switch_to.window(current_tab) 
        profile_menu = self.driver.find_element_by_id('header-profile-menu')
        profile_menu.click() 
        
        setting_link_loc = (By.ID,'profile-settings-link')
        setting_link = self.driver.find_element(*setting_link_loc)
        setting_link = WebDriverWait(self.driver,7).until(
            EC.element_to_be_clickable(setting_link_loc))
        setting_link.click()

        wait.until(EC.url_changes('https://login.yahoo.com/account/personalinfo'))

        change_password_loc = (By.LINK_TEXT,'Account Security')
        change_password = self.driver.find_element(*change_password_loc)
        change_password.click()

        change_password_loc = (By.PARTIAL_LINK_TEXT,'Change password')
        change_password = self.driver.find_element(*change_password_loc)
        change_password = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(change_password_loc))
        change_password.click()

    def test_password_count(self):                          #if only doing one test need to use run_test_ not just test_ 
        actions = ActionChains(self.driver)
        action_tab = actions.send_keys(Keys.TAB)

        new_password_field = self.driver.find_element_by_id('cpwd-password')
        password_status_message_element = self.driver.find_element_by_id('cpwd-error-password')

        bad_chars = ['\n','\t','\r','\x0b','\x0c']
        for char in bad_chars:
            password_characters = string.printable.replace(char,'')
        count_password_characters = 0
        password_status_message = ""
        password = ""

        while (password_status_message == "WEAK_PASSWORD") or (count_password_characters == 0):
            if password_status_message == "" :
                one_character = random.choice(password_characters)
                new_password_field.send_keys(one_character)
                action_tab.perform()
                new_password_field.click()
                time.sleep(0.25)
                password_status_message = password_status_message_element.get_attribute('data-error')
                password = one_character + password
                count_password_characters += 1   
            if password_status_message == "WEAK_PASSWORD":
                one_character = random.choice(password_characters)
                new_password_field.click()
                new_password_field.send_keys(one_character)
                time.sleep(0.25)                                                            #needed to give password message time to load, could use EC text to be present, maybe
                password_status_message = password_status_message_element.get_attribute('data-error')
                password = one_character + password
                count_password_characters += 1
            elif password_status_message == "None":
                break
    
        num_password_characters_client_desires = 7

        self.assertGreaterEqual(count_password_characters,num_password_characters_client_desires) 

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":                      
    unittest.main()  
