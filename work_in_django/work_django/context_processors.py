from .models import Product, Category
from django.db.models import F


def contents(request):
    context = {
        'mob': Product.objects.all() if Product.objects.all() else [],
        'categories': Category.objects.all() if Category.objects.all() else [],
        'limited': Product.objects.filter(limited_edition=True),
        'first_products': Product.objects.order_by('id')[:6],
    }
    return context
