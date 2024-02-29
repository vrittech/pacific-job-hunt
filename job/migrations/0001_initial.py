# Generated by Django 4.1 on 2024-02-29 04:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('image', models.ImageField(upload_to='jobs/category/images')),
                ('slug', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.jobcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(max_length=250)),
                ('position', models.CharField(max_length=200)),
                ('level', models.CharField(choices=[('intern', 'Intern'), ('junior', 'Junior'), ('mid', 'Mid'), ('senior', 'Senior'), ('', '')], default='', max_length=50, null=True)),
                ('required_number', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('timing', models.CharField(choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('remote', 'Remote')], default='full_time', max_length=20)),
                ('salary', models.IntegerField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='job.jobcategory')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
    ]