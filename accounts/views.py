from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User
from exams.models import Exam


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        role = request.POST.get("role")

        user = User.objects.create_user(
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

            if user.role == "teacher":
                return redirect("teacher_dashboard")
            elif user.role == "student":
                return redirect("student_dashboard")
            else:
                return redirect("admin_dashboard")

        else:
            return render(request, "accounts/login.html", {"error": "Invalid username or password"})

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def student_dashboard(request):
    return render(request, "accounts/student_dashboard.html")
from django.contrib.auth.decorators import login_required

@login_required
def teacher_dashboard(request):
    return render(request, "accounts/teacher_dashboard.html")
@login_required
def create_exam(request):

    if request.method == "POST":
        title = request.POST.get("title")

        Exam.objects.create(
            title=title,
            created_by=request.user
        )

        return redirect("teacher_dashboard")

    return render(request, "accounts/create_exam.html")