from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_access_first_page(self):
        # Marcelo abriu o navegador e acessou a página do app
        self.browser.get('http://localhost:8000')

        #No título do navegador aparece GPS, que significa Gerenciador de Ordens de Serviço
        self.assertIn('GPS', self.browser.title)
        self.fail('Finish the test!')

        #Na página inicial solicitará login e senha

if __name__ == '__main__':
    unittest.main()