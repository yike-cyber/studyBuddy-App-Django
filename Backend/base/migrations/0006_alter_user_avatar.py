# Generated by Django 5.0.3 on 2024-06-03 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_replymessage_options_message_liker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatar.svg', null=True, upload_to='images'),
        ),
    ]
