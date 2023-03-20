import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class SearchTests(unittest.TestCase):
     
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path= r'D:\Automatizacion programas\SeleniumPython\chromedriver.exe')
        driver = cls.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(30)

    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME,"q")
        search_field.clear()
        search_field.send_keys('tee')
        search_field.submit()

    
    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME,"q")
        search_field.clear()
        search_field.send_keys('salt shaker')
        search_field.submit()

        products = driver.find_elements(By.XPATH,'/html/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
        self.assertEqual(1,len(products))


     


        
    @classmethod
    def tearDownClass(cls):
        #cierra ventana y todas sus pestanas
        cls.driver.quit()



    