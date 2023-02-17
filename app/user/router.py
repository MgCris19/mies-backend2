from app.user.views.user_has_profile_views import UserProfilenViewSet
from rest_framework.routers import DefaultRouter

from app.user.views.user_views import UsuarioViewSet

router = DefaultRouter()

router.register('/usuario', UsuarioViewSet, basename='usuario')
router.register('/usuario-perfil', UserProfilenViewSet, basename='usuario-perfil')

urlpatterns = router.urls
