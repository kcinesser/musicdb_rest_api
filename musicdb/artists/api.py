from artists.models import Artist
from rest_framework import viewsets, permissions
from .serializers import ArtistSerializer
from songs.serializers import SongSerializer


class ArtistViewset(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = ArtistSerializer

    def get_queryset(self):
        return self.request.user.artists.all().order_by('name')

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
