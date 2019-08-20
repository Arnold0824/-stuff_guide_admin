# Register your models here.
from django.contrib.admin import register, ModelAdmin
from app.models import *
from django.contrib.auth import get_permission_codename
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType

def add_content(modeladmin, request, queryset):
    return HttpResponseRedirect("/app/content/add/")

@register(Content)
class ContentAdmin(ModelAdmin):
    list_display = ('headline', 'cate', 'book_of_cate', 'pub_date')

    def book_of_cate(self, obj):
        return ("%s" % (obj.cate.book.name))

    search_fields = ['headline', 'id']
    book_of_cate.short_description = '手册名'
    # raw_id_fields = ("cate",)


@register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name','farther', 'book_of_cate', 'pub_date','content', 'is_valid')
    def content(self,obj):
        content_name = obj.content_set.all()
        if content_name:
            content_name = content_name[0]
        else:
            content_name = '暂无详细内容'
        return ("%s" % (content_name))

    def book_of_cate(self, obj):
        return ("%s" % (obj.book.name))

    def make_published(self, request, queryset):
        queryset.update(is_valid=1)
        self.message_user(request, "成功审核")

    def make_unpublished(self, request, queryset):
        queryset.update(is_valid=0)
        self.message_user(request, "成功取消审核")

    def has_valid_permission(self, request):
        """Does the user have the valid permission?"""
        opts = self.opts
        codename = get_permission_codename('valid', opts)
        return request.user.has_perm('%s.%s' % (opts.app_label, codename))

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        super().save_model(request, obj, form, change)

    # list_editable = ['is_valid']
    exclude = ('is_valid',)
    actions = ['make_published','make_unpublished']
    search_fields = ['name', 'id']
    book_of_cate.short_description = '手册名'
    make_published.short_description = "批量审核"
    make_published.allowed_permissions = ('valid',)
    make_unpublished.allowed_permissions = ('valid',)
    make_unpublished.short_description = "批量取消审核"


@register(Book)
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


admin.site.register(Tag)
admin.AdminSite.site_header = "员工手册管理"
admin.AdminSite.site_title = "员工手册管理"

# register(User)
