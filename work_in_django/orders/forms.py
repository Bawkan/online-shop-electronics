from django import forms
from orders.models import Order, Delivery


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['full_name', 'phone', 'email', 'city', 'address',
                  'password', 'new_password']

        widgets = {
            'full_name': forms.TextInput(
                attrs={
                    'data-validate': 'require',
                    'maxlength': 50,
                    'placeholder': 'ФИО',
                    'class': 'form-input',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'data-validate': 'require',
                    'maxlength': 15,
                    'placeholder': 'номер телефона',
                    'class': 'form-input'
                }
            ),

            'email': forms.TextInput(
                attrs={
                    'data-validate': 'require',
                    'maxlength': 50,
                    'placeholder': 'имейл',
                    'class': 'form-input'
                }
            ),

            "password": forms.TextInput(
                attrs={
                    'maxlength': 50,
                    'placeholder': 'Тут можно изменить парол',
                    'class': 'form-input',
                }
            ),

            "new_password": forms.TextInput(
                attrs={
                    'maxlength': 50,
                    'placeholder': 'Введите пароль повторно',
                    'class': 'form-input',
                }
            ),

            'city': forms.TextInput(
                attrs={
                    'maxlength': 50,
                    'placeholder': 'Ваш город',
                    'class': 'form-input',
                }
            ),

            'address': forms.TextInput(
                attrs={
                    'maxlength': 150,
                    'placeholder': 'Адрес доставки',
                    'class': 'form-input'
                }
            )
        }


class DeliveryForm(forms.ModelForm):

    class Meta:
        model = Delivery
        fields = ['name', 'price']
