# Generated by Django 4.1 on 2024-05-22 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0019_delete_jobsbookmark'),
    ]

    operations = [
        migrations.DeleteModel(
            name='JobsApply',
        ),
    ]