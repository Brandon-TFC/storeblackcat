
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orden', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='ordenID',
            field=models.CharField(default='', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
