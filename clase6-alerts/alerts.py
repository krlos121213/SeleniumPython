import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class CompareProducts(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
        executable_path=r'D:\Automatizacion programas\SeleniumPython\chromedriver.exe')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_compare_products_removal_alert(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME,'q')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

        driver.find_element(By.CLASS_NAME,'link-compare').click()
        #encontrar un elemento por el texto del enlace
        driver.find_element(By.LINK_TEXT,'Clear All').click()

        alert = driver.switch_to.alert
        alert_text = alert.text

        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)

        alert.accept()
   
    def tearDown(self):
        # cierra ventana y todas sus pestanas
        self.driver.quit()
    


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output='reportes', report_name='clase6'))
