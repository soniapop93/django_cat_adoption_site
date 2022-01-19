from re import U
from django.utils import __path__
from . import views

urlpatterns = [
    path('',views.index, name='index'),
]