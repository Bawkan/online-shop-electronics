from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView, FormView
from .filters import ProductFilter
from .models import Product, Category
from .forms import ProfileForm, CommentForm, UserUpdateForm
from .services import load_profile
from cart.forms import CartAddProductForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(TemplateView):
    """Home page"""
    model = Product
    template_name = 'web/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AboutView(ListView):
    model = Product
    template_name = 'web/about.html'
    context_object_name = 'object'


class AccountView(ListView):
    model = User
    template_name = 'web/account.html'


class CatalogView(ListView):
    model = Product
    template_name = 'web/catalog.html'
    context_object_name = 'object'


def popular_product(request):
    popular = Product.objects.all().order_by('-price')
    context = {
        'popular': popular
    }
    return render(request, 'web/popular.html', context)


def product_list(request):
    f = ProductFilter(request.GET, queryset=Product.objects.all())
    return render(request, 'web/fitler.html', {'filter': f})


def search_product(request):

    if request.method == 'GET':
        search = request.GET.get('search')
        if search:
            products = Product.objects.filter(title__icontains=search)
            return render(request, 'web/search.html', {'product': products})
        else:
            return render(request, 'web/search.html', {})


class ProductDetail(DetailView):
    template_name = 'web/product.html'
    slug_field = 'pk'
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            if request.user.is_authenticated:
                form.user = request.user
                form.name = request.user.username
                form.email = request.user.email
            else:
                form.name = request.POST.get('name')
                form.email = request.POST.get('email')
            form.products = self.get_object()
            form.save()
            return redirect('work_django:product', pk=self.kwargs.get('pk'))
        else:
            return render(request, 'web/product.html',
                          {'product': Product.objects.get(id=self.kwargs.get('pk')), 'form': form})


def main(request, slug):
    mob = Product.objects.filter(category__slug=slug)
    category = Category.objects.all()
    return render(request, 'web/catalog.html', {'mob': mob, 'category': category})


def product_detail(request, id, slug):
    product = Product.objects.filter(id=id, slug=slug)
    context = {
        'cart_product_form': CartAddProductForm()
    }
    return render(request, 'web/product.html', {'pro': product,
                                                'cart_product_form': context})


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'web/profile.html'


class ProfileUpdateView(LoginRequiredMixin, TemplateView, FormView):
    u_form = UserUpdateForm()
    form = ProfileForm()
    template_name = 'web/profileAvatar.html'

    def post(self, request):
        post_data = request.POST or None
        file_data = request.FILES or None
        profile = load_profile(request.user)
        u_form = UserUpdateForm(post_data, instance=request.user)
        form = ProfileForm(post_data, file_data, instance=profile)

        if u_form.is_valid() and form.is_valid():
            u_form.save()
            form.save()
            messages.success(request, 'Профиль успешно сохранен')
            return HttpResponseRedirect(reverse_lazy('work_django:profile'))
        context = self.get_context_data(
            u_form=u_form,
            form=form,
        )
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


def historyorder(request):
    return render(request, 'web/historyorder.html')


def oneorder(request):
    return render(request, 'web/oneorder.html')


def payment(request):
    return render(request, 'web/payment.html')


class DiscountView(ListView):
    model = Product
    template_name = 'web/sale.html'
    context_object_name = 'discount'
