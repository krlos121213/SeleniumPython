import unittest
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class LanguageOptions(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(
            executable_path=r'D:\Automatizacion programas\SeleniumPython\chromedriver.exe')
        driver = cls.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_select_language(self):
        exp_option = ['English', 'French', 'German']
        act_options = []

        select_language = Select(self.driver.find_element(By.ID, 'select-language'))

        self.assertEqual(3, len(select_language.options))

        for option in select_language.options:
            act_options.append(option.text)

        #otra forma del for
        #active_options = [option.text for option in select_language.options]

        
        self.assertListEqual(exp_option, act_options)

        self.assertEqual('English', select_language.first_selected_option.text)

        #seleccionar valor de una lista
        select_language.select_by_visible_text('German')

        self.assertTrue('store=german' in self.driver.current_url)

        self.assertEqual('German', select_language.first_selected_option.text) 

        #otra opcioon para seleccionar atravez del indice  

        select_language.select_by_index(0)    


    @classmethod
    def tearDownClass(cls):
        # cierra ventana y todas sus pestanas
        cls.driver.quit()
        cls.driver.implicitly_wait(3)


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output='reportes', report_name='clase5'))
