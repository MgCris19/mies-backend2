
from app.menu.views.menu_has_screen_views import MenuScreenViewSet
from app.menu.views.menu_views import MenuViewSet
from app.menu.views.screen_views import ScreenViewSet
from app.menu.views.menu_has_screen_views import MenuScreenViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('/menu', MenuViewSet, basename='menu')
router.register('/screen', ScreenViewSet, basename='screen')
router.register('/menu-pantalla', MenuScreenViewSet, basename='menu-pantalla')

urlpatterns = router.urls