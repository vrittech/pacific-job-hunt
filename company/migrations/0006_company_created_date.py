# Generated by Django 4.1 on 2024-06-02 06:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_remove_company_type_company_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
