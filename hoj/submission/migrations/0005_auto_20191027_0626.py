# Generated by Django 2.2.6 on 2019-10-27 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0004_auto_20191026_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='lang',
            field=models.CharField(choices=[('c', 'C'), ('cpp', 'C++'), ('python', 'Python')], default='cpp', max_length=10),
        ),
        migrations.AlterField(
            model_name='submission',
            name='memory',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='submission',
            name='time',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='submission',
            name='verdict',
            field=models.IntegerField(default=0),
        ),
    ]
