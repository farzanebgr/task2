# Generated by Django 4.1 on 2022-08-28 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productionsApp', '0018_alter_productsvisit_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productgallery',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productgallery', to='productionsApp.products', verbose_name='محصول'),
        ),
    ]
