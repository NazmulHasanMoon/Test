# Generated by Django 2.2.6 on 2019-10-22 07:58

import ckeditor_uploader.fields
import django.contrib.postgres.fields
from django.db import migrations, models
import problems.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('difficulty', models.CharField(max_length=100)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, size=None)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('time_limit', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=1), size=None)),
                ('memory_limit', models.IntegerField(default=256)),
                ('input_file', models.FileField(upload_to=problems.models.path_to_save)),
                ('output_file', models.FileField(upload_to=problems.models.path_to_save)),
                ('no_of_submissions', models.IntegerField(default=0)),
                ('no_of_accepted', models.IntegerField(default=0)),
            ],
        ),
    ]
