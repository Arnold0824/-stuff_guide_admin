# Generated by Django 2.2.3 on 2019-08-06 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name_plural': '手册'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['order'], 'verbose_name_plural': '目录'},
        ),
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['-pub_date'], 'verbose_name_plural': '手册内容'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name_plural': '标签'},
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Tag'),
        ),
        migrations.AlterField(
            model_name='category',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
