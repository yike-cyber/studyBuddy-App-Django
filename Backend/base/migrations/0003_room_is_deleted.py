# Generated by Django 5.0.3 on 2024-06-03 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_roomlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]