# Generated by Django 4.1.6 on 2023-03-04 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('work_django', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='Ф.И.О.')),
                ('phone', models.IntegerField(verbose_name='номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='имейл')),
                ('city', models.CharField(max_length=100, verbose_name='город')),
                ('address', models.CharField(max_length=250, verbose_name='адресс')),
                ('password', models.CharField(blank=True, max_length=50, null=True, verbose_name='пароль')),
                ('new_password', models.CharField(blank=True, max_length=50, null=True, verbose_name='новый_пароль')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='цена')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work_django.product', verbose_name='товар')),
            ],
        ),
    ]
