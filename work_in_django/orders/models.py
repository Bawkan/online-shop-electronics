from django.db import models
from work_django.models import Product


class Order(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='Ф.И.О.')
    phone = models.IntegerField(verbose_name='номер телефона')
    email = models.EmailField(verbose_name='имейл')
    city = models.CharField(max_length=100, verbose_name='город')
    address = models.CharField(max_length=250, verbose_name='адресс')
    password = models.CharField(max_length=50, blank=True, null=True, verbose_name='пароль')
    new_password = models.CharField(max_length=50, blank=True, null=True, verbose_name='новый_пароль')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='заказ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='товар')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quatity


class Delivery(models.Model):
    order_delivery = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='доставка')
    name = models.CharField(max_length=50, verbose_name='способ доставки')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=str)

    def __str(self):
        return self.name

