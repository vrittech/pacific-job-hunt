# Generated by Django 4.2.13 on 2024-07-02 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smtp_server_address', models.CharField(max_length=300)),
                ('email_address', models.EmailField(max_length=300)),
                ('password', models.CharField(max_length=2000)),
                ('port', models.PositiveIntegerField()),
                ('required_authentication', models.BooleanField(default=True)),
                ('security', models.CharField(choices=[('None', 'None'), ('SSL', 'SSL'), ('TSL', 'TSL')], default='None', max_length=200)),
                ('smtp_username', models.CharField(blank=True, max_length=100, null=True)),
                ('verify_smtp_certificate', models.BooleanField(default=False)),
            ],
        ),
    ]
