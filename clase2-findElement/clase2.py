import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePageTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path= r'D:\Automatizacion programas\SeleniumPython\chromedriver.exe')
        driver = cls.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)
    
    def test_search_text_field(self):
        driver = self.driver
        search_field = driver.find_element(By.ID,"search")
    

    def test_search_text_field_by_name(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME,"q")

    
    def test_search_text_field_by_class_name(self):
        driver = self.driver
        search_field = driver.find_element(By.CLASS_NAME,"input-text")

    def test_search_button_enabled(self):
        driver = self.driver
        button = driver.find_element(By.CLASS_NAME,"button")
    
    def test_banner_images(self):
        driver = self.driver
        banner_list = driver.find_element(By.CLASS_NAME,"promos")
        banners = banner_list.find_elements(By.TAG_NAME,'img')
        self.assertEqual(3, len(banners))

    def test_vip_promo(self):
        driver = self.driver
        vip_promo = driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[3]/a/img")

    def test_shopping_cart(self):
        driver = self.driver
        shopping_cart_icon = driver.find_element(By.CSS_SELECTOR,"div.header-minicart span.icon")


   

    @classmethod
    def tearDownClass(cls):
        #cierra ventana y todas sus pestanas
        cls.driver.quit()


if __name__=="__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output ='reportes', report_name = 'clase2'))