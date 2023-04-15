from django.test import TestCase
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.urls import reverse


class RegistrationTestCase(TestCase):

    def test_registration(self):
        data = {
            'username': 'username',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'password1': 'qwerty',
            'password2': 'qwerty',
            'email': 'test@mail.ru',
            'city': 'asd',
            'number': '890'
        }
        for invalid_data in data:
            form = RegisterForm(data=data)
            self.failIf(form.is_valid())
            

class AuthenTicationTestCase(TestCase):
    
    def setUp(self):
        self.username = 'username'
        self.password = 'qwerty'
        self.user = User.objects.create_user(username=self.username, 
                                             password=self.password)

    def test_authentication(self):
        response = self.client.post(reverse('authentications:login'), {'username': self.username, 
                                                                        'password': self.password})
        self.assertRedirects(response, reverse('work_django:home'))
