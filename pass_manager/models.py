from django.db import models
from django.utils.text import slugify


class Folder(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class PassCard(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, blank=True, related_name='folder_card')
    name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    site = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
