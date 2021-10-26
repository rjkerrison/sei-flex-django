from django.db import models
from artists.models import Artist

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=50)
    cover_image = models.CharField(max_length=200)
    album_artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, null=True, default=None
    )

    def __str__(self):
        return f"{self.title} by {self.album_artist.name} ({self.id})"
