# Generated by Django 4.1 on 2024-05-22 07:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('job', '0013_delete_profession'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobsApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='job_seekers', to='job.jobs')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apply_jobs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='jobsapply',
            constraint=models.UniqueConstraint(fields=('user', 'job'), name='unique_user_job_apply'),
        ),
    ]