from django.db import models

# Create your models here.
class UrlSlug(models.Model):
    url = models.CharField(max_length=255)
    slug = models.CharField(max_length=15)
