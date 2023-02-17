from rest_framework.routers import DefaultRouter
from app.economyActivity.views import TypeActivityEconomicViewSet, EntrepreneurShipActivityEconomicViewSet, EntrepreneurshipByActivityeconomicViewSet

router = DefaultRouter()
router.register('/tipoacteconomica', TypeActivityEconomicViewSet,basename='tipoacteconomica')
router.register('/emptipo_acteconomica', EntrepreneurShipActivityEconomicViewSet,basename='emptipo_acteconomica')
router.register('/emprendimientos_por_tipoacteconomica', EntrepreneurshipByActivityeconomicViewSet,basename='emprendimientos_por_tipoacteconomica')

urlpatterns = router.urls
