# Generated by Django 5.0.3 on 2024-06-05 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_alter_message_audio_alter_message_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='replymessage',
            name='image',
            field=models.ImageField(null=True, upload_to='files/replied_messages/replied_image_messages'),
        ),
    ]
