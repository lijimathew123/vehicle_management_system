# Generated by Django 4.2.3 on 2023-09-20 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access_vehicle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('user', 'user')], max_length=20),
        ),
    ]
