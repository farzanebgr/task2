# Generated by Django 4.0.6 on 2022-08-15 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productionsApp', '0013_alter_productsrating_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='numbers',
            field=models.IntegerField(default=1, verbose_name='تعداد'),
        ),
    ]
