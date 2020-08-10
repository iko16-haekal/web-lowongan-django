from django.db import models
from slugger import AutoSlugField

# Create your models here.


class Job(models.Model):
    judul = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from="judul")
    kantor = models.CharField(max_length=200)
    lokasi = models.CharField(max_length=200)
    deskripsi_singkat = models.TextField()
    deskripsi = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.judul
