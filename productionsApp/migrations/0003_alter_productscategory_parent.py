# Generated by Django 4.0.6 on 2022-08-04 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productionsApp', '0002_categoryparent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productscategory',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='productionsApp.categoryparent', verbose_name='دسته بندی والد'),
        ),
    ]
