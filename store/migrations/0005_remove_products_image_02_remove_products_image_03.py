# Generated by Django 4.0.4 on 2023-06-23 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_shippingaddress_order_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='image_02',
        ),
        migrations.RemoveField(
            model_name='products',
            name='image_03',
        ),
    ]
