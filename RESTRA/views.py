from django.shortcuts import render
# from django.http import HttpResponse
from formapp.models import menu,specials,Gallery


def index(request):
    menus = menu.objects.all()
    special_items = specials.objects.all()
    gallery_item = Gallery.objects.all()

    return render(request,'index.html',{"menu":menus,'special_items':special_items,'gallery_items':gallery_item})
