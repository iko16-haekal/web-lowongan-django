from django.shortcuts import render
from .models import Job

# Create your views here.
def index(request):
    return render(request, "index.html")


def jobs(request):
    konteks = {
        "jobs": Job.objects.all(),
    }

    return render(request, "jobs.html", konteks)


def detail(request, slug):
    job = Job.objects.filter(slug=slug)
    for jobs in job:
        slug = jobs.slug

    konteks = {"job": job, "slug": slug}
    return render(request, "detail.html", konteks)

