from django.core.urlresolvers import resolve
from django.test import TestCase
from django.contrib.auth.views import login, logout


class HomePageTest(TestCase):

    def test_root_url_resolves_to_login_view(self):
        found = resolve('/')
        self.assertEqual(found.func, login)

    def test_login_return_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'login.html')

    def test_root_url_resolves_to_logout_view(self):
        found = resolve('/sair/')
        self.assertEqual(found.func, logout)
