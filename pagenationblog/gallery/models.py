from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length =255)
    description = models.TextField()
    image = models.ImageField(upload_to = '')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def short_description(self):
        return ' '.join(self.description.split()[:2])+'....'

    def __str__(self):
        return self.name


