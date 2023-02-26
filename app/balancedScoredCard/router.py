from rest_framework.routers import DefaultRouter
from app.balancedScoredCard.views import PerspectiveViewSet

router = DefaultRouter()
router.register('/perspectiva', PerspectiveViewSet, basename='perspectiva')

urlpatterns = router.urls
