from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    image = models.ImageField(upload_to='image', blank=True, verbose_name='изображение')
    name = models.CharField(max_length=50, verbose_name='название', db_index=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('work_django:gory', kwargs={'slug': self.slug})

    # class SubCategory(models.Model):
    #     # title
    #     # slug
    #     parent = models.ForeignKey(Category, on_delete=models.CASC, related_name='sub_categories')


class Product(models.Model):

    MOBILE = 'mobile'
    PK = 'pk'
    NOTEBOOK = 'notebook'
    ACCESSORIES = 'accessories'
    BAGS = 'bags'
    CAMERAS = 'cameras'
    CLOTHINGS = 'clothings'
    FURNITURE = 'furniture'
    LIGHTINGS = 'lightings'
    TRENDS = 'trends'
    MORE = 'more'

    CATEGORY_CHOICES = {
        (MOBILE, 'mobile'),
        (PK, 'pk'),
        (NOTEBOOK, 'notebook'),
        (ACCESSORIES, 'accessories'),
        (BAGS, 'bags'),
        (CAMERAS, 'cameras'),
        (CLOTHINGS, 'clothings'),
        (FURNITURE, 'furniture'),
        (LIGHTINGS, 'lightings'),
        (TRENDS, 'trends'),
        (MORE, 'more')
    }

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categorys')
    image = models.ImageField(upload_to='files/', blank=True, verbose_name='изображение')
    title = models.CharField(max_length=50, verbose_name='название', db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2,
                                              verbose_name='скидка в процентах')
    description = models.TextField(max_length=500, verbose_name='описание')
    available = models.BooleanField(default=True)
    limited_edition = models.BooleanField(default=True, verbose_name='Ограниченный тираж')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    slug = models.SlugField(max_length=200, db_index=True)
    blog = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default=MOBILE)
    discount_from = models.DateField(null=True, blank=True, verbose_name='скидка с')
    discount_to = models.DateField(null=True, blank=True, verbose_name='скидка до')

    def get_absolute_url(self):
        return reverse('work_django:product_detail', args=[self.id, self.slug])

    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug',),)

    def __str__(self):
        return self.title

    def get_item_price_after_discount(self):
        return (self.price * self.discount_percentage)/100

    def now(self):
        now = self.discount_to
        if now:
            return now

    def get_total_discount_item_price(self):
        return self.price - self.get_item_price_after_discount()


class Comment(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users', blank=True, null=True)
    name = models.CharField(max_length=50, verbose_name='название')
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    text = models.TextField(max_length=2500, verbose_name='текст')
    email = models.EmailField(max_length=50, verbose_name='имейл')
    creat_date = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    avatar = models.ImageField(upload_to='images/', verbose_name='изображение', blank=True, null=True)
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    number = models.IntegerField(verbose_name='номер телефона', null=True, blank=True)
    email = models.EmailField(max_length=50, blank=True, null=True, verbose_name='имейл')
    password = models.CharField(max_length=50, blank=True, null=True, verbose_name='пароль')
    new_passeord = models.CharField(max_length=50, blank=True, null=True, verbose_name='новый_пароль')


class RegisterModel(models.Model):
    city = models.CharField(max_length=50, blank=True)
    number = models.CharField(max_length=10, null=True, blank=True)
