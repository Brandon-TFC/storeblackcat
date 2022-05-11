
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import orden.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carts', '0010_alter_cartproduct_managers'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[(orden.models.OrdenStatus['CREATED'], 'CREATED'), (orden.models.OrdenStatus['PAYED'], 'PAYED'), (orden.models.OrdenStatus['COMPLETED'], 'COMPLETED'), (orden.models.OrdenStatus['CANCELED'], 'CANCELED')], default=orden.models.OrdenStatus['CREATED'], max_length=40)),
                ('envio_total', models.DecimalField(decimal_places=2, default=10, max_digits=9)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
