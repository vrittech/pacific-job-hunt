# Generated by Django 4.1 on 2024-06-02 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0015_alter_jobs_company'),
        ('jobapply', '0002_jobsapply_cover_letter_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobsapply',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_seekers', to='job.jobs'),
        ),
    ]
