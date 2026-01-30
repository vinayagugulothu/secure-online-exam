def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("student_dashboard")   # Redirect only here for now
        else:
            return render(request, "accounts/login.html", {"error": "Invalid username or password"})

    return render(request, "accounts/login.html")
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        role = request.POST.get("role")

        # 🔹 Check if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, "accounts/register.html", {
                "error": "Username already exists. Please choose another."
            })

        User.objects.create_user(
            username=username,
            password=password,
            role=role
        )

        return redirect("login")

    return render(request, "accounts/register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("student_dashboard")
        else:
            return render(request, "accounts/login.html", {"error": "Invalid username or password"})

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def student_dashboard(request):
    return render(request, "accounts/student_dashboard.html")
