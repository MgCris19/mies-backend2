from rest_framework.routers import DefaultRouter
from app.entrepreneurShip.views import EntrepreneurshipViewSet, EntrepreneurshipByEntrepreneurViewSet

router = DefaultRouter()
router.register('/emprendimiento', EntrepreneurshipViewSet, basename='emprendimiento')
router.register('/emprendimientos_por_emprendedor', EntrepreneurshipByEntrepreneurViewSet, basename='emprendimientos_por_emprendedor')

urlpatterns = router.urls