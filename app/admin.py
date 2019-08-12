# Register your models here.
from django.contrib.admin import register, ModelAdmin
from app.models import *
from app.admin_site import admin_site


@register(Content, site=admin_site)
class ContentAdmin(ModelAdmin):
    list_display = ('headline', 'cate', 'book_of_cate', 'pub_date')

    def book_of_cate(self, obj):
        return ("%s" % (obj.cate.book.name))

    search_fields = ['headline', 'id']
    book_of_cate.short_description = '手册名'
    raw_id_fields = ("cate",)


@register(Category, site=admin_site)
class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'book_of_cate', 'pub_date')

    def book_of_cate(self, obj):
        return ("%s" % (obj.book.name))

    search_fields = ['name', 'id']
    book_of_cate.short_description = '手册名'


@register(Book, site=admin_site)
class BookAdmin(ModelAdmin):
    list_display = ('name', 'cates', 'cate_num', 'pub_date')
    search_fields = ['name', 'id']

    def cates(self, obj):
        all_cates = [x.name for x in obj.category_set.all()]
        return all_cates

    def cate_num(self, obj):
        return ("%s" % (obj.category_set.count()))

    cates.short_description = '所有目录'
    cate_num.short_description = '目录内容数'


admin_site.register(Tag)
