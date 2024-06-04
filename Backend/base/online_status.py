from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(user_logged_in)
def update_online_status(sender, user, request, **kwargs):
    user.is_online = True
    user.save()

@receiver(user_logged_out)
def clear_online_status(sender, user, request, **kwargs):
    user.is_online = False
    user.save()