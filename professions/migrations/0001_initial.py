# Generated by Django 4.2.13 on 2024-06-19 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profession/images')),
                ('slug', models.CharField(blank=True, max_length=250, unique=True)),
            ],
        ),
    ]
