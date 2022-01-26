from django.shortcuts import render, get_object_or_404
from .models import Cat, Cat_Details


def index(request):
    latest_cat_list = Cat.objects.order_by('-pub_date')[:5]
    context = {
        'latest_cat_list': latest_cat_list,
    }
    return render(request,'adoptions/index.html', context)

def detail(request, cat_id):
    cat = Cat.objects.get(pk=cat_id)
    cat_details = Cat_Details.objects.get(details=cat.pk)
    return render(request, 'adoptions/detail.html', {'cat':cat, 'cat_details':cat_details})