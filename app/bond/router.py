from rest_framework.routers import DefaultRouter
from app.bond.views import BondViewSet, BondByEntrepreneurViewSet

router = DefaultRouter()
router.register('/bonos', BondViewSet, basename='bonos')
router.register('/bonos_por_emprendedor', BondByEntrepreneurViewSet, basename='bonos_por_emprendedor')
urlpatterns = router.urls

