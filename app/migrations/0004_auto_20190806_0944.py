# Generated by Django 2.2.3 on 2019-08-06 09:44

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190806_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='手册内容'),
        ),
    ]
