from rest_framework import serializers
from songs.models import Song

# Song Serializer


class SongSerializer(serializers.ModelSerializer):
    artist_name = serializers.CharField(
        read_only=True, source="get_artist_name")
    file = serializers.SerializerMethodField()

    class Meta:
        model = Song
        fields = ['id', 'title', 'spotify_id', 'youtube_id', 'artist_id',
                  'album', 'genre', 'difficulty', 'notes', 'instrument', 'status', 'created_at', 'artist_name', 'file']

    def file(self, obj):
        return "test"
