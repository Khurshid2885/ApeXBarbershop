from django.contrib.auth import logout, login
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

from accounts.forms import LoginForm, RegisterForm


def register_view(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()

            # Adding to Client Group by Default
            client_group = Group.objects.get(name="client")
            user.groups.add(client_group)

            login(request, user)
            return redirect("services:home")

        return render(request, "accounts/register.html", {"form": form})

    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            response = form.custom_login(request)
            if response:
                return response

    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("accounts:login_view")
