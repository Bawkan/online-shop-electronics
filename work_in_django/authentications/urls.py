from django.urls import path
from django.contrib.auth.decorators import login_required
from authentications.views import (register_view, AuthenticationView,
                                   Logoutview, PasswordChangeView)


app_name = 'authentications'

urlpatterns = [
    path('register/',
         register_view, name='register'),
    path('login/',
         AuthenticationView.as_view(redirect_authenticated_user=True),
         name='login'),
    path('logout/', Logoutview.as_view(), name='logout'),
    path('change/',
         login_required(PasswordChangeView.as_view()),
         name='change')
]
