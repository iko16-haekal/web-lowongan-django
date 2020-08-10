from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from jobsPortal.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="home"),
    path("jobs/", jobs, name="jobs"),
    path("summernote/", include("django_summernote.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
