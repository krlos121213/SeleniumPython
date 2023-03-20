import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class HelloWorld(unittest.TestCase):

    # con @classmethod y cls corremoss todas las pruebas en una sola ventana
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path= r'D:\Automatizacion programas\SeleniumPython\chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10)
    
    def test_hello_world(self):
        driver = self.driver
        driver.get('https://google.com')

    def test_visit_wikipedia(self):
        driver = self.driver
        driver.get('https://wikipedia.org')

    @classmethod
    def tearDownClass(cls):
        #cierra ventana y todas sus pestanas
        cls.driver.quit()


"""
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r'D:\Automatizacion programas\SeleniumPython\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(10)
    
    def test_hello_world(self):
        driver = self.driver
        driver.get('https://google.com')

    def test_visit_wikipedia(self):
        driver = self.driver
        driver.get('https://wikipedia.org')

    def tearDown(self):
        #cierra ventana y todas sus pestanas
        self.driver.quit()
"""
    
if __name__=="__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output ='reportes', report_name = 'hello-world-report'))