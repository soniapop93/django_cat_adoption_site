from django.shortcuts import render, redirect
from .forms import RegisterForm


def signup(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/cats")
    else:
        form = RegisterForm()

    return render(response, "registration/signup.html", {"form":form})


def profile(response):
    if response.user.is_authenticated:
        return render(response, "users/profile.html")
    else:
        return redirect('/accounts/login')
