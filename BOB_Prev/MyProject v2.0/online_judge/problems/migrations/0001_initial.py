# Generated by Django 2.2.7 on 2019-12-26 16:44

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone
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
                ('title', models.CharField(max_length=100, null=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('author', models.CharField(max_length=100, null=True)),
                ('tester', models.CharField(max_length=100, null=True)),
                ('editorial', models.TextField()),
                ('tags', models.CharField(max_length=100, null=True)),
                ('difficulty', models.CharField(max_length=100, null=True)),
                ('time_limit', models.IntegerField(blank=True, null=True)),
                ('memory_limit', models.IntegerField(blank=True, null=True)),
                ('permit_languages', models.CharField(max_length=100, null=True)),
                ('judge_input', models.FileField(upload_to=problems.models.upload_path_handler)),
                ('judge_output', models.FileField(upload_to=problems.models.upload_path_handler)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
