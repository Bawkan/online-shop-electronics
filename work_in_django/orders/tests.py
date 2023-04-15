from django.test import TestCase
from .forms import OrderForm


class OrderValidTestCase(TestCase):

    def test_order(self):

        data = {'full_name': 'Ivanov',
                'phone': '890',
                'email': 'test@mail.ru',
                'city': 'Moscow',
                'address': 'prospect mira'
                }

        for form in data:
            form = OrderForm(data=data)
            self.assertTrue(form)
            
