import unittest
from selenium import webdriver
from api_data_mock import ApiDataMock
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By


class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'D:\Automatizacion programas\SeleniumPython\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/customer/account/create/')

    def test_new_user(self):
        driver = self.driver

        self.assertEqual('Create New Customer Account', driver.title)

        first_name = driver.find_element(By.ID,'firstname')
        middle_name = driver.find_element(By.ID,'middlename')
        last_name = driver.find_element(By.ID,'lastname')
        email_address = driver.find_element(By.ID,'email_address')
        password = driver.find_element(By.ID,'password')
        confirm_password = driver.find_element(By.ID,'confirmation')
        news_letter_subscription = driver.find_element(By.ID,'is_subscribed')
        submit_button = driver.find_element(By.XPATH,'//*[@id="form-validate"]/div[2]/button/span/span')

        self.assertTrue(first_name.is_enabled()
                        and middle_name.is_enabled()
                        and last_name.is_enabled()
                        and email_address.is_enabled()
                        and password.is_enabled()
                        and confirm_password.is_enabled()
                        and news_letter_subscription.is_enabled()
                        and submit_button.is_enabled())

        first_name.send_keys(ApiDataMock.first_name)
        middle_name.send_keys(ApiDataMock.middle_name)
        last_name.send_keys(ApiDataMock.last_name)
        email_address.send_keys(ApiDataMock.email_address)
        password.send_keys(ApiDataMock.password)
        confirm_password.send_keys(ApiDataMock.password)
        submit_button.click()

    def tearDown(self):
        self.driver.implicitly_wait(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'api' ))