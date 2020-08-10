from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Job

# Register your models here.
class JobAdmin(SummernoteModelAdmin):
    summernote_fields = "deskripsi"
    list_per_page = 5
    search_fields = ["judul"]


admin.site.register(Job, JobAdmin)
