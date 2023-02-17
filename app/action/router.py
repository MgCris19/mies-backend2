from rest_framework.routers import DefaultRouter
from app.action.views import ActionViewSet

router = DefaultRouter()
router.register('/action', ActionViewSet, basename='action')

urlpatterns = router.urls
