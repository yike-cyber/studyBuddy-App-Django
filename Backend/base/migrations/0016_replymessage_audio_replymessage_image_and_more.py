# Generated by Django 5.0.3 on 2024-06-05 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_alter_message_audio_alter_message_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='replymessage',
            name='audio',
            field=models.FileField(null=True, upload_to='files/replied_messages/replied_audio_messages'),
        ),
        migrations.AddField(
            model_name='replymessage',
            name='image',
            field=models.ImageField(null=True, upload_to='files/replied_images/replied_image_messages'),
        ),
        migrations.AddField(
            model_name='replymessage',
            name='video',
            field=models.FileField(null=True, upload_to='files/replied_messages/replied_video_messages'),
        ),
    ]
