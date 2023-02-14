from django.db import models
from django.contrib.auth.models import User


def get_image_url(instance, filename):
    return f'{instance.user.username}/profile/{filename}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True)

    image = models.ImageField(upload_to=get_image_url, blank=True)

    # def __str__(self) -> str:
    #     return f'{self.image}'
