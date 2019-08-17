from django.db import models

# Create your models here.
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField('目录名称', max_length=70)
    farther = models.ForeignKey('Category', verbose_name='上一级目录(可为空)', on_delete=models.CASCADE, blank=True, null=True)
    pub_date = models.DateTimeField('发布时间', auto_now_add=True)
    order = models.IntegerField('排列顺序-升序')
    book = models.ForeignKey('Book', verbose_name='所属手册', on_delete=models.CASCADE)
    is_valid = models.IntegerField('是否审核通过', choices=((1, '审核通过'), (0, '未审核')), default=0)

    def __str__(self):
        return self.name



    class Meta:
        verbose_name = '目录'
        verbose_name_plural = '目录'
        ordering = ['order']
        permissions = [
                    ("valid_category", "可以审核"),
                ]

class Book(models.Model):
    name = models.CharField('手册', max_length=70)
    pub_date = models.DateTimeField('发布时间', auto_now_add=True, null=True)
    tag = models.ForeignKey('Tag', verbose_name='标签(可为空)', on_delete=models.SET_NULL, blank=True, null=True)
    cover_img = models.ImageField('封面图片', upload_to='cover_img/', default='', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '手册'
        verbose_name_plural = '手册'

    def get_all_cate(self):
        category_set = self.category_set.all()
        data = []
        for x in category_set:
            if x.farther or not x.is_valid:
                continue
            son = self.find_son(x, category_set)
            tmp = {'name': x.name, 'son': son, 'id': x.id, 'order_id': x.order, 'is_valid': x.is_valid,
                   'pub_date': x.pub_date}
            data.append(tmp)
        return data

    def find_son(self, cate_obj, all_cate_set):
        data = []
        for x in all_cate_set:
            if cate_obj.id == x.farther_id:
                son = self.find_son(x, all_cate_set)
                data.append({'name': x.name, 'son': son, 'id': x.id, 'order_id': x.order, 'is_valid': x.is_valid,
                             'pub_date': x.pub_date})
        return data


class Tag(models.Model):
    name = models.CharField('名称', max_length=50)
    pub_date = models.DateTimeField('发布时间', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'


class Content(models.Model):
    pub_date = models.DateTimeField('发布时间', auto_now_add=True)
    headline = models.CharField('标题', max_length=200)
    content = RichTextUploadingField('手册内容')
    cate = models.ForeignKey('Category', verbose_name='所属目录', on_delete=models.CASCADE, db_index=True)

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name = '手册内容'
        verbose_name_plural = '手册内容'
        ordering = ['-pub_date']
