from django.urls import path
from .views import (CatalogView, AccountView, ProfileView,
                    AboutView, main, HomePageView,
                    historyorder, oneorder, payment, DiscountView,
                    product_detail, ProductDetail, search_product, 
                    ProfileUpdateView, product_list,
                    popular_product, categories)

app_name = 'work_django'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('<int:id>/<slug:slug>/', product_detail, name='product_detail'),
    path('catalog/<int:pk>/', ProductDetail.as_view(), name='product'),
    path('popular/', popular_product, name='popular'),
    path('about/', AboutView.as_view(), name='aboutt'),
    path('categories/<slug:slug>/', main, name='gory'),
    path('account/', AccountView.as_view(), name='account'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('historyorder/', historyorder, name='historyorder'),
    path('oneorder/', oneorder, name='oneorder'),
    path('payment/', payment, name='payment'),
    path('sale/', DiscountView.as_view(), name='sale'),
    path('filter/', product_list, name='filter'),
    path('search/', search_product, name='search'),
    path('profilesave/', ProfileView.as_view(), name='avatar'),
    path('categories/<slug:slug>/', categories, name='sub_category'),
    ]
