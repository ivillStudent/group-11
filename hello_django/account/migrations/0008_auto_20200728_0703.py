# Generated by Django 3.0.8 on 2020-07-28 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0007_auto_20200728_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='creditcard', to=settings.AUTH_USER_MODEL),
        ),
    ]
