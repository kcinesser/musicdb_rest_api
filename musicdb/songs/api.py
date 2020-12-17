from songs.models import Song
from rest_framework import viewsets, permissions
from .serializers import SongSerializer


class SongViewset(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = SongSerializer

    def perform_update(self, serializer):
        print(serializer.validated_data)
        serializer.save()

    def get_queryset(self):
        return Song.objects.filter(artist_id__user_id=self.request.user)

    def perform_create(self, serializer):
        serializer.save()
