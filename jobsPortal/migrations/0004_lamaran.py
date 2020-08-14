# Generated by Django 2.2.12 on 2020-08-14 12:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsPortal', '0003_auto_20200810_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='lamaran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul_job', models.CharField(max_length=200)),
                ('slug_job', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=200)),
                ('telepon', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('cv', models.FileField(upload_to='cv/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['.pdf', '.doc', '.docx'])])),
            ],
        ),
    ]
