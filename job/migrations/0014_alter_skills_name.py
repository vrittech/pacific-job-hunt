# Generated by Django 4.1 on 2024-05-27 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0013_delete_profession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
