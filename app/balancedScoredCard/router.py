from rest_framework.routers import DefaultRouter
from app.balancedScoredCard.views import PerspectiveViewSet, IndicatorViewSet,ObjectiveViewSet,BscViewSet

router = DefaultRouter()
router.register('/perspectiva', PerspectiveViewSet, basename='perspectiva')
router.register('/indicadores', IndicatorViewSet, basename='indicadores')
router.register('/objetivos', ObjectiveViewSet, basename='objetivos')
router.register('/bsc', BscViewSet, basename='bsc')

urlpatterns = router.urls
