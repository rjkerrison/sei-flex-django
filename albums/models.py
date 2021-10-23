from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    cover_image = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.id})"
