# Generated by Django 4.2.13 on 2024-06-19 12:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('job', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.PositiveIntegerField()),
                ('company_name', models.CharField(max_length=1500)),
                ('designation', models.CharField(max_length=1000)),
                ('joined_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('still_work', models.BooleanField(default=False)),
                ('job_categories', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='work_experience', to='job.jobcategory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_experience', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
