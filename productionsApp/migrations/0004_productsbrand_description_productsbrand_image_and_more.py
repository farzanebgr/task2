# Generated by Django 4.0.6 on 2022-08-07 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productionsApp', '0003_alter_productscategory_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsbrand',
            name='description',
            field=models.TextField(null=True, verbose_name='توضیحات برند'),
        ),
        migrations.AddField(
            model_name='productsbrand',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='brands/', verbose_name='تصویر محصول'),
        ),
        migrations.AlterField(
            model_name='productsbrand',
            name='title',
            field=models.CharField(db_index=True, max_length=200, verbose_name='نام برند'),
        ),
    ]
