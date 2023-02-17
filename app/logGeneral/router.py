from rest_framework.routers import DefaultRouter
from app.logGeneral.views import logGeneralViewSet

router = DefaultRouter()
router.register('/logGeneral', logGeneralViewSet,
                basename='logGeneral')


urlpatterns = router.urls