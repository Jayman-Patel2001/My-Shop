# Generated by Django 3.1.1 on 2020-10-03 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_order_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items_json',
            field=models.CharField(max_length=499),
        ),
    ]
