# from django.shortcuts import render, redirect
#
#
# def signup(request):
#     return render(request)


from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.
def signup(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/cats")
    else:
        form = RegisterForm()

    return render(response, "registration/signup.html", {"form":form})

