# Generated by Django 5.0.3 on 2024-06-02 20:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_user_avatar_user_bio_user_name_alter_user_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='liker',
            field=models.ManyToManyField(blank=True, related_name='likers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message',
            name='num_of_likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='message',
            name='replier',
            field=models.ManyToManyField(blank=True, related_name='repliers', to=settings.AUTH_USER_MODEL),
        ),
    ]
