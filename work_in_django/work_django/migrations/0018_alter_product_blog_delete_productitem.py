# Generated by Django 4.1.6 on 2023-03-13 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_django', '0017_alter_product_blog_alter_product_discount_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='blog',
            field=models.CharField(choices=[('notebook', 'notebook'), ('bags', 'bags'), ('pk', 'pk'), ('clothings', 'clothings'), ('mobile', 'mobile'), ('furniture', 'furniture'), ('trends', 'trends'), ('lightings', 'lightings'), ('accessories', 'accessories'), ('more', 'more'), ('cameras', 'cameras')], default='mobile', max_length=50),
        ),
        migrations.DeleteModel(
            name='ProductItem',
        ),
    ]
