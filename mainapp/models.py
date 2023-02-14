from django.db import models
from django.contrib.auth.models import User


class Folder(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='allfolders')
    name = models.CharField(max_length=100)
    folder = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, related_name='folder_within')

    def __str__(self) -> str:
        return f'{self.name}'


class File(models.Model):
    folder = models.ForeignKey(
        Folder, on_delete=models.CASCADE, related_name='allfiles')

    def get_file_url(instance, filename):
        return f'files/{instance.folder.user.username}/{instance.folder.name}/{filename}'
    file = models.FileField(upload_to=get_file_url)

    def __str__(self):
        return f'{self.file}'
