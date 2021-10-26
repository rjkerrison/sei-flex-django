from django.db import models
from artists.models import Artist

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=50)
    cover_image = models.CharField(max_length=200)
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        null=True,
        default=None,
        related_name="albums",
    )

    def __str__(self):
        return f"{self.title} by {self.artist.name} ({self.id})"
