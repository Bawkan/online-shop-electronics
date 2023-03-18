from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from authentications.forms import AuthenticationForms, RegisterForm, MyPasswordChangeForm
from work_django.models import RegisterModel
from django.contrib import messages


def register_view(request):
    """ Function for registration """

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            city = register_form.cleaned_data['city']
            number = register_form.cleaned_data['number']
            RegisterModel.objects.create(
                city=city,
                number=number,
            )
            username = register_form.cleaned_data['username']
            raw_password = register_form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
        return render(request, 'authentication/register.html', {'form': form})


class AuthenticationView(LoginView):

    """Class for Authentication"""

    form_class = AuthenticationForms
    template_name = 'authentication/login.html'
    success_url = reverse_lazy('/')


class PasswordChangeView(FormView):
    form_class = MyPasswordChangeForm
    template_name = 'authentication/change_password.html'
    success_url = reverse_lazy('authentications:change')

    def get_success_url(self):
        return self.success_url

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.INFO, 'Пароль успешно сохранен')
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)


class Logoutview(LogoutView):
    next_page = '/'
