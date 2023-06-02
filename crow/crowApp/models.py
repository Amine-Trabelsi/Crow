from django.db import models
from django.utils import timezone
# Create your models here.
class CrowPost(models.Model):
    title = models.CharField(max_length=100)
    published_date = models.DateTimeField(default=timezone.now)
    data = models.TextField()

    def __str__(self):
        return self.title