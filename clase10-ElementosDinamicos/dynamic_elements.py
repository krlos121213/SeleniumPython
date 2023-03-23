import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class DinamicElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
        executable_path=r'D:\Automatizacion programas\SeleniumPython\chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element(By.LINK_TEXT,'Disappearing Elements').click()

    def test_name_elements(self):
        driver = self.driver

        options = []
        menu = 5
        tries = 1

        while len(options) < 5:
            options.clear()


            for i in range(menu):
                try:
                    option_name = driver.find_element(By.XPATH,f"/html/body/div[2]/div/div/ul/li[{i+1}]/a")
                    options.append(option_name.text)
                    print(options)
                except:
                    print(f"Option numer {i+1} is not found")
                    tries +=1
                    driver.refresh()
        print(f"finished in {tries} tries")
        

        #otra manera tomando todoos los elementos que contienen el tag li
        """elements = driver.find_elements_by_tag_name('li')

        while len(elements) < 5:
            #Si los elementos que encontré son menores a 5 recargo la pagina y vuelvo a "contar" los elementos de la lista
            print('Elementos en la lista', len(elements))
            driver.refresh()
            elements = driver.find_elements_by_tag_name('li')
            #Sumo otro intento
            intentos += 1
            #Espero 1 segundo para que poder ver cuántas veces ha recargado
            sleep(1)
        """



        
        
    
           
    def tearDown(self):
        # cierra ventana y todas sus pestanas
        self.driver.quit()
    


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output='reportes', report_name='clase10'))