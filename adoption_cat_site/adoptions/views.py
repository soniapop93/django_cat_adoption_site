from django.shortcuts import render
from .models import Cat, Cat_Details
from users import views

class CatWithPhoto:
    def __init__(self, cat_object, cat_image):
        self.cat_obj = cat_object
        self.cat_img = cat_image

def index(request):
    latest_cat_list = []
    cat_list = Cat.objects.order_by('-pub_date')
    for cat in cat_list:
        cat_details = Cat_Details.objects.get(details=cat.pk)
        latest_cat_list.append(CatWithPhoto(cat, cat_details.cat_photo))
    context = {
        'latest_cat_list': latest_cat_list,
    }
    return render(request,'adoptions/index.html', context)

def detail(request, cat_id):
    cat = Cat.objects.get(pk=cat_id)
    cat_details = Cat_Details.objects.get(details=cat.pk)
    return render(request, 'adoptions/detail.html', {'cat':cat, 'cat_details':cat_details})

def contact(request):
    return render(request, 'adoptions/contact.html')

def recently_adopted(request):
    return render(request,'adoptions/recently_adopted.html')

def adopt_cat(request, cat_id):
    cat = Cat.objects.get(pk=cat_id)
    cat_details = Cat_Details.objects.get(details=cat.pk)
    return render(request, 'adoptions/adopt_cat.html', {'cat':cat, 'cat_details':cat_details})