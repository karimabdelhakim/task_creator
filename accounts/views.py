from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout, login
from .forms import LoginForm, RegisterForm


def login_view(request):
    """View for logging users in"""

    if request.user.is_authenticated:
        return redirect("task:create")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return redirect("task:create")
    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {"form": form})


def register_view(request):
    """View for registering users"""

    if request.user.is_authenticated:
        return redirect("task:create")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:login")
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


def logout_view(request):
    """View for user logout"""
    logout(request)
    return redirect("accounts:login")
