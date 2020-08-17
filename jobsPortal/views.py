from django.shortcuts import render, redirect
from .models import Job
from .forms import FormLamar, SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, "index.html")


def jobs(request):
    konteks = {
        "jobs": Job.objects.all().order_by("-id"),
    }

    return render(request, "jobs.html", konteks)


def detail(request, slug):
    job = Job.objects.filter(slug=slug)

    konteks = {"job": job, "slug": slug}
    return render(request, "detail.html", konteks)


@login_required(login_url=settings.LOGIN_URL)
def lamar(request, slug):
    job = Job.objects.filter(slug=slug)
    for job in job:
        title = job.judul
    konteks = {
        "form": FormLamar(
            initial={
                "slug_job": slug,
                "judul_job": title,
                "email": request.user.email,
                "user": request.user,
            }
        ),
        "slug": slug,
    }

    return render(request, "lamar.html", konteks)


def signup(request):
    form = SignUpForm()
    if request.POST:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "user created successfully")
            return redirect("/login")
    konteks = {"form": form}
    return render(request, "registration/signup.html", konteks)

