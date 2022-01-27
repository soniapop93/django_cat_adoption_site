from . import views
from django.urls import path

app_name= 'adoptions'
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:cat_id>/', views.detail, name='detail' ),
]