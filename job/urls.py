from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from jobsPortal.views import *
from django.contrib.auth.views import LoginView, LogoutView
from jobsPortal.forms import loginForm

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="home"),
    path("jobs/", jobs, name="jobs"),
    path("jobs/detail/<slug:slug>/", detail, name="detailJobs"),
    path("jobs/lamar/<slug:slug>/", lamar, name="lamarJobs"),
    path("signup/", signup, name="signup"),
    path("login/", LoginView.as_view(authentication_form=loginForm), name="login"),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
    path("summernote/", include("django_summernote.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
