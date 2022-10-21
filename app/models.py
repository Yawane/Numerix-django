from django.db import models

# Create your models here.
"""
Prroject
- Titre
- Slug
- Image
- Description
- Thème
- date de MAJ
"""


class Project(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    thumbnail = models.ImageField(blank=True, null=True, upload_to='project')
    description = models.TextField(blank=True)
    theme = models.CharField(max_length=32)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True)

    def __str__(self):
        return self.title
