from rest_framework.routers import DefaultRouter
from app.balancedScoredCard.views import IndicatorViewSet

router = DefaultRouter()
router.register('/indicadores', IndicatorViewSet, basename='indicadores')
urlpatterns = router.urls