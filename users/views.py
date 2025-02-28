from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout  # noqa: F401
from .forms import LoginForm, RegisterForm
from loguru import logger


def sign_in(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "users/login.html", {"form": form})

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            authenticate(request, username=form.username, password=form.password)
            return redirect("webcamera", permanent=True)
        else:
            return redirect("login")


def sign_out(request):
    # logout()
    pass


def sign_up(request: HttpRequest):
    logger.info(f"Sign up method: {request.method}")
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "users/register.html", {"form": form})

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            logger.info("Form is valid")
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "You have singed up successfully.")
            login(request, user)
            return redirect("webcamera")
        else:
            logger.info("Form is not valid")
            return render(request, "users/register.html", {"form": form})
