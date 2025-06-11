from django.db import models

class Slug(models.Model):
    slug = models.CharField(max_length=10)
    slug_content = models.TextField()
    time_limit = models.TimeField()

    def __str__(self):
        return f"{self.slug} has {self.slug_content} text that has expiry of {self.time_limit}"

# Create your models here.
