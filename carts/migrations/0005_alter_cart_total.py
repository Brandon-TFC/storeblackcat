# Generated by Django 3.2.8 on 2021-10-21 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_cart_cart_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
    ]
