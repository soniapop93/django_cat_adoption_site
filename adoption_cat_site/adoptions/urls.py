from re import U
from django.utils import __path__
from . import views
from django.urls import path

app_name= 'adoptions'
urlpatterns = [
    path('',views.index, name='index'),
]