from django.db.models.signals import post_save
from .handler import create_profile
from django.contrib.auth.models import User

post_save.connect(receiver=create_profile, sender=User)
