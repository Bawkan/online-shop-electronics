from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User


class AuthenticationForms(AuthenticationForm, forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=30, required=False, help_text='Фамилия')
    city = forms.CharField(max_length=30, required=False, help_text='Город')
    number = forms.CharField(max_length=12, required=False, help_text='Номер телефона')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class MyPasswordChangeForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["old_password"].widget = forms.PasswordInput(attrs={"class": "form-input",
                                                                        "placeholder": 'Старый пароль'})
        self.fields["new_password1"].widget = forms.PasswordInput(attrs={"class": "form-input",
                                                                         "placeholder": 'Новый пароль'})
        self.fields["new_password2"].widget = forms.PasswordInput(attrs={"class": "form-input",
                                                                         "placeholder": 'Подтверждение пароля'})
