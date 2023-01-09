from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     raw = kwargs['raw']
#     if not raw:
#         if created:
#             first_name = instance.first_name
#             last_name = instance.last_name
#             name = first_name + ' ' + last_name
#             UserProfile.objects.create(name=name, user=instance)