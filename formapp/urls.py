
from django.urls import path
from . import views

urlpatterns = [
    path('',views.contact,name='contact'),
    path('booktable1',views.booktable1,name='booktable1'),
    path('subscribe',views.subscribe,name='subscribe'),
    ]