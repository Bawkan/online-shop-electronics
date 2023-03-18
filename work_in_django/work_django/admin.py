from django.contrib import admin
from .models import Product, Category, Profile, Comment


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    prepopulated_fields = {"slug": ("name",)}


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'avatar']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id']


admin.site.register(Product, ProductsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Comment, ReviewAdmin)
