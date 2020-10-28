from django.shortcuts import render, redirect
from .models import Job, Lamaran
from .forms import FormLamar, SignUpForm, FormJob
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, "index.html")


def jobs(request):
    jobs = Job.objects.all().order_by("-id")
    if request.GET.get("keyword"):
        jobs = Job.objects.filter(judul__icontains=request.GET.get("keyword"))
    konteks = {
        "jobs": jobs,
    }
    return render(request, "jobs.html", konteks)


def detail(request, id, slug):
    job = Job.objects.filter(slug=slug)
    lamaran = Lamaran.objects.filter(user=request.user, judul=id)
    exist = False
    if lamaran:
        exist = True
    konteks = {"job": job, "slug": slug, "exist": exist}
    return render(request, "detail.html", konteks)


@login_required(login_url=settings.LOGIN_URL)
def lamar(request, id, slug):
    if request.POST:
        form = FormLamar(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, "berhasil melamar, semoga diterima di perusahaan kami"
            )
            return redirect("/jobs")

    job = Job.objects.filter(id=id)
    for job in job:
        judul = job.id
    konteks = {
        "form": FormLamar(
            initial={"judul": judul, "email": request.user.email, "user": request.user,}
        ),
        "slug": slug,
    }

    return render(request, "lamar.html", konteks)


@login_required(login_url=settings.LOGIN_URL)
def myLamaran(request):
    lamaran = Lamaran.objects.filter(user=request.user)
    konteks = {"lamaran": lamaran}
    return render(request, "myLamaran.html",konteks)


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

