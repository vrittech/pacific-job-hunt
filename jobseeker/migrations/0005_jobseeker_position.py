# Generated by Django 4.1 on 2024-05-19 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0004_alter_jobsapply_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseeker',
            name='position',
            field=models.CharField(default='', max_length=1500),
            preserve_default=False,
        ),
    ]