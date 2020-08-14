from django.forms import ModelForm
from django import forms
from jobsPortal.models import Lamaran


class FormLamar(ModelForm):
    class Meta:
        model = Lamaran
        fields = "__all__"

        widgets = {
            "judul_job": forms.HiddenInput({"class": "form-control"}),
            "slug_job": forms.HiddenInput({"class": "form-control"}),
            "user": forms.HiddenInput({"class": "form-control"}),
            "telepon": forms.NumberInput({"class": "form-control"}),
            "email": forms.EmailInput({"class": "form-control"}),
            "cv": forms.FileInput({}),
        }

