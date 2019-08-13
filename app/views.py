from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views import View
from django.views.generic import ListView
from app.models import *


# Create your views here.

class BookView(View):
    def get(self, request):
        params = request.GET
        book_id = int(params.get('book_id', 0))
        if not book_id:
            data = []
            for x in Book.objects.all():
                data.append({
                    'book_id': x.id,
                    'cover_img': x.cover_img.name,
                    'pub_date': x.pub_date,
                    'all_cate': x.get_all_cate(),
                    # ''
                })
        book_obj = Book.objects.get(id=book_id)
        if not book_obj:
            return Http404
        data = {
            'book_id': book_id,
            'cover_img': book_obj.cover_img.name,
            'pub_date': book_obj.pub_date,
            'all_cate': book_obj.get_all_cate(),
            # ''
        }
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False})


class ContentView(View):
    def get(self, request):
        params = request.GET
        cate_id = int(params.get('cate_id'))
        content_obj = Content.objects.get(cate_id__exact=cate_id)
        data = {
            'content': content_obj.content,
            'headline': content_obj.headline,
            'pub_date': content_obj.pub_date,
        }
        return JsonResponse(data)
