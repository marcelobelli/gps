from django.test import TestCase
from django.core.urlresolvers import resolve
from django.contrib.auth.models import User

from gps.core.views import dashboard


class DashBoardTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')


    def test_dashboard_url_resolves_to_dashboard_view(self):
        found = resolve('/dashboard/')
        self.assertEqual(found.func, dashboard)

    def test_access_dashboard_without_login_redirect_to_index(self):
        response = self.client.get('/dashboard/')
        self.assertRedirects(response, '/?next=/dashboard/')


    def test_dashboard_return_correct_html_if_user_is_authenticated(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get('/dashboard/')
        self.assertTemplateUsed(response, 'dashboard.html')
