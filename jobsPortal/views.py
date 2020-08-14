from django.shortcuts import render
from .models import Job
from .forms import FormLamar

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


def lamar(request, slug):
    job = Job.objects.filter(slug=slug)
    for job in job:
        title = job.judul
    konteks = {
        "form": FormLamar(initial={"slug_job": slug, "judul_job": title}),
    }

    return render(request, "lamar.html", konteks)

