# Generated by Django 4.2.13 on 2024-06-17 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_size',
            field=models.CharField(max_length=350, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='location',
            field=models.CharField(max_length=950, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='website',
            field=models.URLField(max_length=300, null=True),
        ),
    ]