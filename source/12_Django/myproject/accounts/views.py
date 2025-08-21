from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings

from .forms import SignupForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def signup(request):
    # POST : 회원가입 처리
    if request.method == "POST":
        form = SignupForm(request.POST)  # ✅ POST 데이터를 포함한 폼 생성
        if form.is_valid():
            user = form.save()  # 사용자와 프로필 모두 저장됨
            return redirect("login")  # 로그인 페이지로 리다이렉트

    # GET : 회원가입 폼 보여주기
    else:
        form = SignupForm()

    # 회원가입 폼 보여주기
    return render(request, "accounts/signup_form.jinja.html", {"form": form})


login = LoginView.as_view(template_name="accounts/login_form.jinja.html")


@login_required
def profile(request):  # 로그인 후에만 접근 가능
    profile, create = Profile.objects.get_or_create(
        user=request.user,
        defaults={
            "phone_number": "",
            "address": "",
        },
    )
    return render(
        request,
        "accounts/profile.jinja.html",
        {"user": request.user, "profile": profile, "is_new_profile": create},
    )


logout = LogoutView.as_view(next_page=settings.LOGIN_URL)
