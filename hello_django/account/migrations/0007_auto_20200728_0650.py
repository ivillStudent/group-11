# Generated by Django 3.0.8 on 2020-07-28 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20200728_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='card_expirationdate',
            field=models.CharField(default='', max_length=7),
        ),
    ]
