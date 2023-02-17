from rest_framework.routers import DefaultRouter
from app.observations.views import ObservationsViewSet

router = DefaultRouter()
router.register('/observations', ObservationsViewSet,
                basename='observations')


urlpatterns = router.urls