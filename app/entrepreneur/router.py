from rest_framework.routers import DefaultRouter
from app.entrepreneur.views import EntrepreneurViewSet, PhoneEntrepreneurViewSet, PhoneTypeViewSet, AssociationEntrepreneurViewSet,PhonebyEntrepreneurViewSet

router = DefaultRouter()
router.register('/emprendedor', EntrepreneurViewSet, basename='emprendedor')
router.register('/emprendedor_asociacion', AssociationEntrepreneurViewSet, basename='emprendedor_asociacion')
router.register('/tipo_telefono', PhoneTypeViewSet, basename='tipo_telefono')
router.register('/telefono_emprendedor', PhoneEntrepreneurViewSet, basename='telefono_emprendedor')
router.register('/telefonos_por_emprendedor', PhonebyEntrepreneurViewSet, basename='telefonos_por_emprendedor')

urlpatterns = router.urls