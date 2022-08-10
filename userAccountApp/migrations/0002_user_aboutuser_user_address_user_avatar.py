# Generated by Django 4.0.6 on 2022-08-09 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAccountApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='aboutUser',
            field=models.TextField(blank=True, null=True, verbose_name='درباره کاربر'),
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='آدرس کاربر'),
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='user/', verbose_name='تصویر نمایه کاربر'),
        ),
    ]
