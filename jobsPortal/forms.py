from django.forms import ModelForm
from django import forms
from jobsPortal.models import Lamaran
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class SignUpForm(UserCreationForm, ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(
        label=("Password"), widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )


class FormLamar(ModelForm):
    class Meta:
        model = Lamaran
        fields = "__all__"

        widgets = {
            "judul_job": forms.HiddenInput({"class": "form-control"}),
            "slug_job": forms.HiddenInput({"class": "form-control"}),
            "user": forms.HiddenInput({"class": "form-control"}),
            "telepon": forms.NumberInput({"class": "form-control"}),
            "email": forms.HiddenInput({"class": "form-control"}),
            "cv": forms.FileInput({"class": "form-control-file"}),
        }


class loginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(
        label=("Password"), widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ["username", "password"]

