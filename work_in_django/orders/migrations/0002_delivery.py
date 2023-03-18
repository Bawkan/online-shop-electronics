# Generated by Django 4.1.6 on 2023-03-04 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='способ доставки')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='доставка')),
            ],
        ),
    ]
