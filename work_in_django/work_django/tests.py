from django.test import TestCase
from django.urls import reverse
from work_django.models import Product
from django.contrib.auth.models import User
from work_django.forms import CommentForm


class HomePageTemmplateViewTestCase(TestCase):

    def test_home_page(self):
        response = self.client.get(reverse('work_django:home'))
        self.assertEqual(response.status_code, 200)


class ProductDetailTestCase(TestCase):

    def test_product_detail(self):
        self.product = Product.objects.create(price=1)
        response = self.client.get(reverse('work_django:product', kwargs={"pk": self.product.pk}))
        self.assertEqual(response.status_code, 200)



class ProfileTestCase(TestCase):

    def setUp(self):
        self.username = 'baba'
        self.password = 'qwerty'
        self.user = User.objects.create_user(username=self.username,
            password=self.password)
        

    def test_profile(self):
       
        response = self.client.post('/profile/',
            {'username': self.username, 
            'password': self.password})
        self.assertEqual(response.status_code, 302)

    def test_profile_not_authentication(self):
        self.client.logout()
        response = self.client.get(reverse('work_django:profile'))
        self.assertEqual(response.status_code, 302)

    
class FormTestCase(TestCase):

    def test_form(self):
        form = {
            'name': '',
            'text': 'Hello',
            'email': 'reis_969@mail.ru'
            }
        my_form = CommentForm(data=form)
        self.failIf(my_form.is_valid())
