import time

from django.test import LiveServerTestCase
from django.contrib.auth.models import User

from selenium import webdriver


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.user = User.objects.create_superuser('marcelo', 'user@gmail.com', 'pass')
        self.browser = webdriver.PhantomJS()

    def tearDown(self):
        self.browser.quit()

    def test_access_first_page_login_and_logout(self):
        # Marcelo abriu o navegador e acessou a página do app
        self.browser.get(self.live_server_url)

        #No título do navegador aparece GPS
        self.assertIn('GPS', self.browser.title)

        #E da página aparece Gerenciador de Ordens de Serviço
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Gerenciador de Prestação de Serviço', header_text)

        #Na página inicial haverá os campos:
        #Login
        login_label = self.browser.find_element_by_xpath('//label[@for="id_username"]').text
        self.assertIn('Usuário', login_label)

        username = self.browser.find_element_by_id('id_username')
        self.assertTrue(username)

        #E Senha
        password_label = self.browser.find_element_by_xpath('//label[@for="id_password"]').text
        self.assertIn('Senha', password_label)

        password = self.browser.find_element_by_id('id_password')
        self.assertTrue(password)

       #E no fim o botão Entrar
        login_button = self.browser.find_element_by_tag_name('button')
        self.assertIn('Entrar', login_button.text)

        # Ao preencher os campos e clicar em Entrar, serei redirecionado para a pagina Dashboard
        username.send_keys('marcelo')
        password.send_keys('pass')
        login_button.click()
        time.sleep(1)

        # Apos carregar a página o título do navegador deve ser GPS - Dashboard
        self.assertIn('GPS - Dashboard', self.browser.title)

        # E da página Dashboard
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Dashboard', header_text)

        # Haverá mensagem dizendo: Olá Marcelo
        greetings_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Olá Marcelo', greetings_text)

        # E um link com o texto Sair
        logout_link = self.browser.find_element_by_tag_name('a')
        self.assertIn('Sair', logout_link.text)

        # Clicando em sair o sistema realizará o logout e voltarei para a tela de login
        logout_link.click()
        time.sleep(1)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Gerenciador de Prestação de Serviço', header_text)
