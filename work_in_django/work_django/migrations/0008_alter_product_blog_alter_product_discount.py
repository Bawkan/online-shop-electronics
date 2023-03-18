# Generated by Django 4.1.6 on 2023-03-11 21:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_django', '0007_alter_product_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='blog',
            field=models.CharField(choices=[('lightings', 'lightings'), ('bags', 'bags'), ('pk', 'pk'), ('cameras', 'cameras'), ('more', 'more'), ('notebook', 'notebook'), ('accessories', 'accessories'), ('mobile', 'mobile'), ('clothings', 'clothings'), ('furniture', 'furniture'), ('trends', 'trends')], default='mobile', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)]),
        ),
    ]
