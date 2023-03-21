import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


class NavigationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
        executable_path=r'D:\Automatizacion programas\SeleniumPython\chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(15)
        driver.get("https://google.com/")

    def test_browser_navigation(self):
        driver = self.driver

        search_field = driver.find_element(By.NAME,'q')
        search_field.clear()
        search_field.send_keys('platzi')
        search_field.submit()


        #retroceder
        driver.back()
        sleep(3)

        #avanzar
        driver.forward()
        sleep(3)

        #refrescar
        driver.refresh()
        sleep(3)
   
    def tearDown(self):
        # cierra ventana y todas sus pestanas
        self.driver.quit()
    


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output='reportes', report_name='clase7'))
