from django.contrib import admin
from orders.models import Order, OrderProduct, Delivery


class OrderProductAdmin(admin.TabularInline):
    model = OrderProduct
    raw_id_fields = ['product']


class DeliveryAdmin(admin.TabularInline):
    model = Delivery
    list_display = ['id', 'name']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone', 'email', 'address',  'city', 'paid',
                    'created', 'updated', 'password', 'new_password']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderProductAdmin, DeliveryAdmin]


admin.site.register(Order, OrderAdmin)
