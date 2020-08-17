# Generated by Django 2.2.12 on 2020-08-16 15:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsPortal', '0004_lamaran'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lamaran',
            name='cv',
            field=models.FileField(upload_to='cv/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['.pdf', '.doc', '.docx', '.jpg', '.jpeg', '.png'])]),
        ),
    ]
