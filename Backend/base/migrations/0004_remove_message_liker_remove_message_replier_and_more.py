# Generated by Django 5.0.3 on 2024-06-02 22:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_message_liker_message_num_of_likes_message_replier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='liker',
        ),
        migrations.RemoveField(
            model_name='message',
            name='replier',
        ),
        migrations.CreateModel(
            name='ReplyMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('replied_text', models.TextField(max_length=2000)),
                ('num_of_likes', models.IntegerField(default=0)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.message')),
                ('replier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
