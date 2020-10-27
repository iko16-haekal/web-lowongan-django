from django.forms import ModelForm
from django import forms
from jobsPortal.models import Lamaran, Job
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


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
            "judul": forms.TextInput({"class": "form-control", "type": "hidden"}),
            "user": forms.TextInput({"class": "form-control", "type": "hidden"}),
            "status": forms.TextInput({"class": "form-control", "type": "hidden"}),
            "telepon": forms.NumberInput({"class": "form-control"}),
            "email": forms.EmailInput({"class": "form-control", "type": "hidden"}),
            "cv": forms.FileInput({"class": "form-control-file"}),
        }


class FormJob(forms.Form, ModelForm):
    deskripsi = forms.CharField(widget=SummernoteWidget())
    slug = forms.CharField(widget=forms.HiddenInput(), label="", required=False)

    class Meta:
        model = Job
        fields = ["judul", "kantor", "lokasi", "deskripsi_singkat", "deskripsi", "slug"]
        widgets = {
            "judul": forms.TextInput({"class": "form-control"}),
            "kantor": forms.TextInput({"class": "form-control"}),
            "lokasi": forms.TextInput({"class": "form-control"}),
            "deskripsi_singkat": forms.Textarea({"class": "form-control"}),
            "slug": forms.HiddenInput({"type": "hidden"}),
        }


class loginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(
        label=("Password"), widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ["username", "password"]

