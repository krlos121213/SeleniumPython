import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class AddRemoveElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
        executable_path=r'D:\Automatizacion programas\SeleniumPython\chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element(By.LINK_TEXT,'Add/Remove Elements').click()
        
    def test_add_remove(self):
        driver = self.driver

        elements_added = int(input("how many elements will you add"))
        elements_removed = int(input("how many elements will you remove"))
        total_elements = elements_added - elements_removed

        add_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/button')
        sleep(3)
        

        for i in range(elements_added):
            add_button.click()
        
        for i in range(elements_removed):
            try:
                delete_button = driver.find_element(By.XPATH,'//*[@id="elements"]/button[1]')
                delete_button.click()
            except:
                print("you are triying to delete more elementes the existent")
                break
        
        if total_elements > 0:
            print(f"there are {total_elements} elements on screen ")
        else:
            print("there 0 are elemnents on screen")
        
        sleep(3)
        


 

   
    def tearDown(self):
        # cierra ventana y todas sus pestanas
        self.driver.quit()
    


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output='reportes', report_name='clase9'))