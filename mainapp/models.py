from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q


class Folder(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='allfolders')
    name = models.CharField(max_length=100)
    folder = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, related_name='folder_within')

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['folder', 'name'], name='unique_folder_within',),
            models.UniqueConstraint(
                fields=['name', 'user'], condition=Q(folder=None), name='unique_folder_dash'),
        ]


class File(models.Model):
    folder = models.ForeignKey(
        Folder, on_delete=models.CASCADE, related_name='allfiles')

    def get_file_url(instance, filename):
        current_url = instance.folder
        path = ''
        while (current_url):
            path = f'{current_url}'+path
            current_url = current_url.folders
        print(current_url)
        # return f'files/{instance.folder.user.username}/{instance.folder.name}/{filename}'
    file = models.FileField(upload_to=get_file_url)
    filename = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'{self.file}'

    def save(self, *args, **kwargs):
        self.filename = self.file.name
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.file.storage.delete(self.file.name)
        super().delete(*args, **kwargs)
