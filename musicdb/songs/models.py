from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .validators.difficulty_validator import validate_difficulty

# Create your models here.


class Song(models.Model):
    INSTRUMENT_CHOICES = [
        ('Guitar', 'Guitar'),
        ('Piano', 'Piano'),
    ]
    STATUS_CHOICES = [
        (1, 'Not Started'),
        (2, 'In Progress'),
        (3, 'Proficient'),
    ]
    GENRE_CHOICES = [
        ('Alternative', 'Alternative'),
        ('Folk', 'Folk'),
        ('Country', 'Country'),
        ('Rock', 'Rock'),
        ('Metal', 'Metal'),
        ('Pop', 'Pop'),
        ('Classical', 'Classical'),
        ('Jazz', 'Jazz'),
    ]

    title = models.CharField(max_length=100)
    spotify_id = models.CharField(max_length=50, unique=True, blank=True)
    artist_id = models.ForeignKey(
        'artists.Artist', related_name="songs", on_delete=models.CASCADE, null=True)
    album = models.CharField(max_length=100, blank=True)
    youtube_id = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, default="")
    instrument = models.CharField(
        max_length=25, choices=INSTRUMENT_CHOICES, default="Guitar")
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    genre = models.CharField(
        max_length=20, choices=GENRE_CHOICES, blank=True, default="")
    difficulty = models.IntegerField(validators=[validate_difficulty],
                                     default=0)
    # uploads =

    def get_artist_name(self):
        return self.artist_id

    def __str__(self):
        return self.title
