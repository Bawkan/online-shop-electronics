# Generated by Django 4.1.6 on 2023-03-05 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_django', '0003_alter_product_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='blog',
            field=models.CharField(choices=[('notebook', 'notebook'), ('trends', 'trends'), ('clothings', 'clothings'), ('accessories', 'accessories'), ('cameras', 'cameras'), ('furniture', 'furniture'), ('bags', 'bags'), ('lightings', 'lightings'), ('pk', 'pk'), ('mobile', 'mobile'), ('more', 'more')], default='mobile', max_length=50),
        ),
    ]
