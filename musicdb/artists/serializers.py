from rest_framework import serializers
from artists.models import Artist
from songs.serializers import SongSerializer

# Artist Serializer


class ArtistSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ('name', 'id', 'spotify_id', 'image_url',
                  'created_at', 'user_id', 'songs')
