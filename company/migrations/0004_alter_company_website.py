# Generated by Django 4.1 on 2024-05-20 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_rename_description_company_about_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='website',
            field=models.URLField(default='', max_length=300),
            preserve_default=False,
        ),
    ]