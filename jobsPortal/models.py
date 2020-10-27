from django.db import models
from slugger import AutoSlugField
from django.core.validators import FileExtensionValidator

# Create your models here.


class Job(models.Model):
    judul = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from="judul", unique=True, blank=True)
    kantor = models.CharField(max_length=200)
    lokasi = models.CharField(max_length=200)
    deskripsi_singkat = models.TextField()
    deskripsi = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.judul


class Lamaran(models.Model):
    judul = models.ForeignKey(Job, on_delete=models.CASCADE)  # hidden
    user = models.CharField(max_length=200)  # hidden
    telepon = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)  # hidden

    cv = models.FileField(
        upload_to="cv/",
        validators=[
            FileExtensionValidator(
                allowed_extensions=["pdf", "doc", "docx", "jpg", "jpeg", "png"]
            )
        ],
    )
    status = models.CharField(max_length=200, default="belum dilihat")

    def __str__(self):
        return self.judul_job
