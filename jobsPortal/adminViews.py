from django.shortcuts import render, redirect
from .models import Job, Lamaran
from .forms import FormLamar, SignUpForm, FormJob
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.conf import settings



@login_required(login_url=settings.LOGIN_URL)
def Admin(request):
    if not request.user.is_superuser or not request.user.is_staff:
        return redirect("/")
    return render(request, "sbadmin/index.html")


@login_required(login_url=settings.LOGIN_URL)
def AdminJob(request):
    jobs = Job.objects.all().order_by("-id")
    if not request.user.is_superuser or not request.user.is_staff:
        return redirect("/")
    if request.GET.get("keyword"):
        jobs = Job.objects.filter(judul__icontains=request.GET.get("keyword"))
    konteks = {"jobs": jobs}
    return render(request, "sbadmin/job.html", konteks)


@login_required(login_url=settings.LOGIN_URL)
def AdminDetailJob(request, slug):
    if not request.user.is_superuser or not request.user.is_staff:
        return redirect("/")
    jobs = Job.objects.filter(slug=slug)

    konteks = {
        "jobs": jobs,
    }
    return render(request, "sbadmin/detailJob.html", konteks)


@login_required(login_url=settings.LOGIN_URL)
def AdminEditJob(request, slug):
    if not request.user.is_superuser or not request.user.is_staff:
        return redirect("/")
    job = Job.objects.get(slug=slug)
    form = FormJob(instance=job, initial={"slug": ""})
    if request.POST:
        form = FormJob(request.POST, request.FILES, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, "berhasil mengubah lowongan")
            return redirect("/admin/jobs")
    konteks = {"form": form}
    return render(request, "sbadmin/admin-edit.html", konteks)


@login_required(login_url=settings.LOGIN_URL)
def AdminAddJob(request):
    if not request.user.is_superuser or not request.user.is_staff:
        return redirect("/")
    form = FormJob()
    if request.POST:
        form = FormJob(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "berhasil menambahkan lowongan")
            return redirect("/admin/jobs")
    konteks = {"form": form}
    return render(request, "sbadmin/admin-add.html", konteks)


@login_required(login_url=settings.LOGIN_URL)
def AdminDeleteJob(request, id):
    if not request.user.is_superuser or not request.user.is_staff:
        return redirect("/")
    if request.POST:
        job = Job.objects.get(id=id)
        job.delete()
        messages.success(request, "berhasil menghapus lowongan")
        return redirect("/admin/jobs")
    else:
        return redirect("/admin/")


@login_required(login_url=settings.LOGIN_URL)
def Pelamar(request):
    if not request.user.is_superuser or not request.user.is_staff:
        return redirect("/")
    if request.POST:
        lamaran = Lamaran.objects.get(id=request.POST.get("id"))
        lamaran.status = request.POST.get("status")
        lamaran.save()
        return redirect("/admin/pelamar")
    konteks = {
        "lamaran": Lamaran.objects.filter(status="belum dilihat").order_by("-id"),
        "diterima": Lamaran.objects.filter(status="diterima").order_by("-id"),
        "dilihat": Lamaran.objects.filter(status="dilihat").order_by("-id"),
    }
    return render(request, "sbadmin/pelamar.html", konteks)
