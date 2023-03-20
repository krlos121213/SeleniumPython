import unittest
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By


class registerNewUser(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path= r'D:\Automatizacion programas\SeleniumPython\chromedriver.exe')
        driver = cls.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)


    def test_new_user(self):
        driver = self.driver
        driver.find_element(By.XPATH,'/html/body/div/div[2]/header/div/div[2]/div/a').click()
        driver.find_element(By.LINK_TEXT,'Log In').click()
       
        create_account_button = driver.find_element(By.XPATH,'/html/body/div/div[2]/div[2]/div/div/div[2]/form/div/div[1]/div[2]/a/span/span')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

        #verificar si estamos en una seccion de la pagina 

        self.assertEqual('Create New Customer Account', driver.title)

        first_name = driver.find_element(By.ID,'firstname')
        middle_name = driver.find_element(By.ID,'middlename')
        last_name = driver.find_element(By.ID,'lastname')
        email_addres = driver.find_element(By.ID,'email_address')
        password = driver.find_element(By.ID,'password')
        confirm_password = driver.find_element(By.ID,'confirmation')
        news_letter_subscription = driver.find_element(By.ID,'is_subscribed')
        submit_button = driver.find_element(By.XPATH,'/html/body/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button/span/span')

        self.assertTrue(first_name.is_enabled() 
                        and middle_name.is_enabled() 
                        and last_name.is_enabled() 
                        and email_addres.is_enabled() 
                        and password.is_enabled() 
                        and confirm_password.is_enabled() 
                        and news_letter_subscription.is_enabled() 
                        and submit_button.is_enabled() )
        
        first_name.send_keys('carlos')
        driver.implicitly_wait(5)
        middle_name.send_keys('andres')
        driver.implicitly_wait(1)
        last_name.send_keys('zapata')
        driver.implicitly_wait(5)
        email_addres.send_keys("asdsad@yopmail.com")
        driver.implicitly_wait(1)
        password.send_keys('1234')
        driver.implicitly_wait(1)
        confirm_password.send_keys('123456')
        driver.implicitly_wait(1)
        news_letter_subscription.click()
        driver.implicitly_wait(1)
        submit_button.click()


    @classmethod
    def tearDownClass(cls):
        #cierra ventana y todas sus pestanas
        cls.driver.quit()
        cls.driver.implicitly_wait(3)

if __name__=="__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output ='reportes', report_name = 'clase4'))