# Generated by Django 3.0.3 on 2020-04-08 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0009_auto_20200408_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
