from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.
class HomePageTest(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_by_url(self):
         response = self.client.get(reverse('home'))
         self.assertEqual(response.status_code, 200)

    def test_tempalte_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')


class SignUpTest(TestCase):
    username = 'testuser'
    email = 'testuser@gmail.com'

    def test_signup_page_status_code(self):
        response  = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_by_url_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_template_use(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_form(self):
        get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
