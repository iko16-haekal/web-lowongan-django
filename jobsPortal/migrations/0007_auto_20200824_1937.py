# Generated by Django 2.2.12 on 2020-08-24 12:37

from django.db import migrations
import slugger.fields


class Migration(migrations.Migration):

    dependencies = [
        ('jobsPortal', '0006_auto_20200817_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='slug',
            field=slugger.fields.AutoSlugField(populate_from='judul', unique=True),
        ),
    ]