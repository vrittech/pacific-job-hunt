# Generated by Django 4.1 on 2024-05-22 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0013_delete_profession'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobseeker', '0016_alter_professionalinformation_profession'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobsBookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='saved_jobs', to='job.jobs')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved_jobs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='jobsbookmark',
            constraint=models.UniqueConstraint(fields=('user', 'job'), name='unique_user_job_saved_application'),
        ),
    ]
