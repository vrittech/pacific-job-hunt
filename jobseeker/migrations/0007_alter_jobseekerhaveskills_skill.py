# Generated by Django 4.1 on 2024-05-19 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_jobs_status'),
        ('jobseeker', '0006_alter_jobsapply_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseekerhaveskills',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobseeker', to='job.skills'),
        ),
    ]