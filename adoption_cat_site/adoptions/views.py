from django.shortcuts import render
from .models import Cat

def index(request):
    latest_cat_list = Cat.objects.order_by('-pub_date')[:5]
    context = {
        'latest_cat_list': latest_cat_list,
    }
    return render(request,'adoptions/index.html', context)