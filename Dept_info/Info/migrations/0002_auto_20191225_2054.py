# Generated by Django 3.0.1 on 2019-12-25 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Info', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Id',
            new_name='SId',
        ),
    ]
