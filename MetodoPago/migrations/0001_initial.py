from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True #Esto lo usuamos para manejar errores

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL), #Almacenar los datos en cache
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilePago',
            fields=[ 
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=50)),
                ('cart_id', models.CharField(max_length=50)),
                ('last4', models.CharField(max_length=4)),
                ('brand', models.CharField(max_length=10)),
                ('default', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
