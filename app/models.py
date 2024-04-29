from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    summary = models.TextField()
    cover_image = models.URLField()
    video_url = models.URLField()