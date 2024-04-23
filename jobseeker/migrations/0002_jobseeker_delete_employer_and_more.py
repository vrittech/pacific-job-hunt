# Generated by Django 4.1 on 2024-04-23 05:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobseeker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobSeeker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv', models.FileField(null=True, upload_to='users/jobseeker/images')),
                ('expected_salary', models.PositiveIntegerField()),
                ('experience', models.PositiveIntegerField()),
                ('job_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='jobseekers', to='job.jobcategory')),
                ('skills', models.ManyToManyField(related_name='jobseekers', through='jobseeker.EmployerHaveSkills', to='job.skills')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='jobseeker', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Employer',
        ),
        migrations.AlterField(
            model_name='employerhaveskills',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobseeker.jobseeker'),
        ),
    ]