from django.shortcuts import render, get_object_or_404
from orders.forms import OrderForm
from orders.models import OrderProduct, Order
from cart.cart import Cart
from orders.tasks import order_created
from django.contrib.auth import get_user


def order_create(request):
    order_s = OrderProduct.objects.all()
    cart = Cart(request)
    post_data = request.POST or None
    if request.method == 'POST':
        form = OrderForm(post_data)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderProduct.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
            order_created.delay(order.id)
            return render(request,
                          'web/payment.html')

    else:
        if request.user.is_authenticated:
            user = get_user(request)
            form = OrderForm(initial={'full_name': user, 'email': user.email})
        else:
            form = OrderForm()
    return render(request, 'orders/order.html', {'form': form, 'order': order_s})
