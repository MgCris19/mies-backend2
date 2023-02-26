from rest_framework.routers import DefaultRouter
from app.balancedScoredCard.views import ObjectiveViewSet


router = DefaultRouter()
router.register('/objetivos', ObjectiveViewSet, basename='objetivos')

urlpatterns = router.urls
