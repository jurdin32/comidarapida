# Generated by Django 3.0.4 on 2022-04-08 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0, verbose_name='Stock'),
        ),
    ]
