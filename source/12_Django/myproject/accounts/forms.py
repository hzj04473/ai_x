from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class SignupForm(UserCreationForm):
    phone_number = forms.CharField(
        label="전화",
        max_length=20,
    )
    address = forms.CharField(
        label="주소",
        max_length=100,
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)  # super() 호출 수정
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
            profile = Profile(
                user=user,
                phone_number=self.cleaned_data["phone_number"],
                address=self.cleaned_data["address"],
            )
            profile.save()

        return user
