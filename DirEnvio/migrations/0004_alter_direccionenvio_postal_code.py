# Generated by Django 4.0.4 on 2022-05-13 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DirEnvio', '0003_alter_direccionenvio_default'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccionenvio',
            name='postal_code',
            field=models.CharField(max_length=6),
        ),
    ]
