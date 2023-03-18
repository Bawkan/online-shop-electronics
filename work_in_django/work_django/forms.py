from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Product, Profile, Comment


class ProductForm(forms.ModelForm):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Product
        fields = '__all__'


class UserUpdateForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'maxlength': 50,
                    'placeholder': 'name*',
                    'class': 'form-input',
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    'maxlength': 50,
                    'placeholder': 'Email',
                    'class': 'form-input',
                }
            ),
        }


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['avatar', 'number', 'password', 'new_passeord']
        exclude = ['user']

        widgets = {
            'number': forms.TextInput(
                attrs={
                    'maxlength': 50,
                    'placeholder': "Телефон",
                    'class': 'form-input',
                }
            ),
            "password": forms.TextInput(
                attrs={
                    'maxlength': 50,
                    'placeholder': 'Password*',
                    'class': 'form-input',
                }
            ),

            "new_passeord": forms.TextInput(
                attrs={
                    'maxlength': 50,
                    'placeholder': 'New password*',
                    'class': 'form-input',
                }
            ),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text', 'email', 'name', 'users']

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'maxlength': 50,
                    'placeholder': 'Name*',
                    'class': 'form-input'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'maxlength': 50,
                    'placeholder': 'Mail*',
                    'class': 'form-input',
                }
            ),
            "text": forms.Textarea(
                attrs={
                    'class': 'form-textarea'
                }
            ),
        }
