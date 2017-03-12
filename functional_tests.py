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

        #No título do navegador aparece GPS
        self.assertIn('GPS', self.browser.title)

        # E da página aparece Gerenciador de Ordens de Serviço
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Gerenciador de Ordens de Serviço', header_text)

        #Na página inicial haverá os campos de login e senha
        username = self.browser.find_element_by_id('username')
        password = self.browser.find_element_by_id('password')
        self.assertIn('Login', username.text)
        self.assertIn('Senha', password.text)

        #O usuário então digitará suas credenciais
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()