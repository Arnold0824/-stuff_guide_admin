from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views import View
from django.views.generic import ListView
from app.models import *
from django.db.models import Q
from django.conf import settings

# Create your views here.

class BookView(View):
    def get(self, request):
        params = request.GET
        book_id = int(params.get('book_id', 0))
        if not book_id:
            data = []
            for x in Book.objects.all():
                img_path = settings.HOST_NAME + settings.MEDIA_URL + x.cover_img.name if x.cover_img else ''
                data.append({
                    'book_id': x.id,
                    'name': x.name,
                    'cover_img': img_path,
                    'pub_date': x.pub_date,
                    'all_cate': x.get_all_cate(),
                    # ''
                })
            return JsonResponse(data, json_dumps_params={'ensure_ascii': False},safe=False)

        book_obj = Book.objects.get(id=book_id)
        if not book_obj:
            return Http404
        data = {
            'book_id': book_id,
            'name': book_obj.name,
            'cover_img': book_obj.cover_img.name,
            'pub_date': book_obj.pub_date,
            'all_cate': book_obj.get_all_cate(),
            # ''
        }
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False})


class ContentView(View):
    def get(self, request):
        params = request.GET
        c_id = int(params.get('id'))
        content_obj = Content.objects.filter(id=c_id)
        if not content_obj:
            data = {'status':-1,
                    'content':'',
                    'headline':'',
                    'pub_date':''}
        else:
            content_obj = content_obj[0]
            if '/media/' in content_obj.content:
                content = content_obj.content.replace('/media/',settings.HOST_NAME + settings.MEDIA_URL)
            else:
                content = content_obj.content
            pre, next = content_obj.get_pre_next_content()
            data = {
                'content': content,
                'headline': content_obj.headline,
                'pub_date': content_obj.pub_date,
                'status':1,
                'pre': pre,
                'next': next,
            }
        return JsonResponse(data)

class SearchView(View):
    def get(self,request):
        params = request.GET
        kw = params.get('kw')
        cate_obj = Category.objects.filter(Q(name__contains=kw)|Q(id__contains=kw))
        data = []
        for x in cate_obj:
            data.append({
                'cate_id': x.id,
                'content_ids':x.get_all_content_ids(),
                'name': x.name,
                'pub_date': x.pub_date,
            })
        return JsonResponse(data,safe=False)