from rest_framework import routers
from .api import ArtistViewset

router = routers.DefaultRouter()
router.register('api/artists', ArtistViewset, 'artists')

urlpatterns = router.urls
