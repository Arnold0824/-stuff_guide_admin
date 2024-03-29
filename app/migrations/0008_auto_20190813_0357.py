# Generated by Django 2.2.3 on 2019-08-13 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_book_cover_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_valid',
            field=models.IntegerField(choices=[('审核通过', 1), ('未审核', 0)], default=0, verbose_name='是否审核通过'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_img',
            field=models.ImageField(default='', null=True, upload_to='cover_img/', verbose_name='封面图片'),
        ),
        migrations.AlterField(
            model_name='category',
            name='farther',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Category', verbose_name='上一级目录(可为空)'),
        ),
    ]
