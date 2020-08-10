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

