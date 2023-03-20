import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class AssertionsTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path= r'D:\Automatizacion programas\SeleniumPython\chromedriver.exe')
        driver = cls.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(30)
    
    def test_search_text_field_by_name(self):
        self.assertTrue(self.is_element_present(By.NAME,"q"))

    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID,"select-language"))

    

    @classmethod
    def tearDownClass(cls):
        #cierra ventana y todas sus pestanas
        cls.driver.quit()


    def is_element_present(self, how, what):
        #how tipo selector
        #what valor que tiene
        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
            return False
        return True




