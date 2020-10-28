from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from jobsPortal.views import *
from jobsPortal.adminViews import *
from django.contrib.auth.views import LoginView, LogoutView
from jobsPortal.forms import loginForm
from django.contrib.auth.decorators import permission_required

urlpatterns = [
    ################################### ADMIN VIEWS #########################################
    path("admin-django/", admin.site.urls),
    path("admin/", Admin, name="admin"),
    path("admin/jobs", AdminJob, name="adminJob"),
    path("admin/jobs/tambah", AdminAddJob, name="adminAddJob"),
    path("admin/jobs/detail/<slug:slug>/", AdminDetailJob, name="adminDetailJobs"),
    path("admin/jobs/ubah/<slug:slug>/", AdminEditJob, name="adminEditJob"),
    path("admin/jobs/hapus/<int:id>/", AdminDeleteJob, name="adminDeleteJob"),
    path("admin/pelamar", Pelamar, name="pelamar"),
    ################################### INDEX VIEWS #########################################
    path("", index, name="home"),
    path("my/", myLamaran, name="my"),
    path("jobs/", jobs, name="jobs"),
    path("jobs/detail/<int:id>/<slug:slug>", detail, name="detailJobs"),
    path("jobs/lamar/<slug:slug>/<int:id>", lamar, name="lamarJobs"),
    ################################### AUTH VIEWS #########################################
    path("signup/", signup, name="signup"),
    path("login/", LoginView.as_view(authentication_form=loginForm), name="login"),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
    ################################### tool  ##############################################
    path("summernote/", include("django_summernote.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
