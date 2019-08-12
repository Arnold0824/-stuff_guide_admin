from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_header = '员工手册管理后台'
    site_title = '员工手册管理后台'

admin_site = MyAdminSite(name='myadmin')
