from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100, blank=True)
    spotify_id = models.CharField(max_length=50, blank=True)
    user_id = models.ForeignKey(
        User, related_name="artists", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
