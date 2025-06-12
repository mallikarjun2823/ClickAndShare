from django.db import models
from django.utils import timezone

class Slug(models.Model):
    slug = models.CharField(max_length=10)
    slug_content = models.TextField()
    time_limit = models.DateTimeField()
    created_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.slug} has {self.slug_content} text that's created at {self.created_time} and expires at {self.time_limit}"
