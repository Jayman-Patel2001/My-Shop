# Generated by Django 3.1.1 on 2020-10-05 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20201004_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.IntegerField(default=0, max_length=100),
        ),
    ]
