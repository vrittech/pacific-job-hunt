# Generated by Django 4.2.13 on 2024-06-25 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0004_educationlevel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='education_level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='education.educationlevel'),
        ),
    ]
