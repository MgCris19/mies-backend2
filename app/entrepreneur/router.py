from rest_framework.routers import DefaultRouter
from django.urls import path, include
from app.entrepreneur.views import EntrepreneurViewSet, PhoneEntrepreneurViewSet, PhoneTypeViewSet, AssociationEntrepreneurViewSet,PhonebyEntrepreneurViewSet
from app.entrepreneur.apiEntrepreneur import getEntrepreneurByName
router = DefaultRouter()
router.register('/emprendedor', EntrepreneurViewSet, basename='emprendedor')
router.register('/emprendedor_asociacion', AssociationEntrepreneurViewSet, basename='emprendedor_asociacion')
router.register('/tipo_telefono', PhoneTypeViewSet, basename='tipo_telefono')
router.register('/telefono_emprendedor', PhoneEntrepreneurViewSet, basename='telefono_emprendedor')
router.register('/telefonos_por_emprendedor', PhonebyEntrepreneurViewSet, basename='telefonos_por_emprendedor')

urlpatterns = [
    path('', include(router.urls)),
    path('/emprendedor/search', getEntrepreneurByName),
]
