from django.db import models

# Create your models here.


class ShortUrl(models.Model):
    short = models.CharField(max_length=100)
    original_url = models.URLField()

    def __str__(self):
        return self.short
