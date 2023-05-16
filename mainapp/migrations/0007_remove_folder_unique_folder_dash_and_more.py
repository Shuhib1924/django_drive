# Generated by Django 4.1.5 on 2023-02-18 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_remove_folder_folder_within_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='folder',
            name='unique_folder_dash',
        ),
        migrations.AddConstraint(
            model_name='folder',
            constraint=models.UniqueConstraint(condition=models.Q(('folder', None)), fields=('name', 'user'), name='unique_folder_dash'),
        ),
    ]
