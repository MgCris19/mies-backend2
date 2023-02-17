from app.profile.views.profile_has_screen_has_action_views import ProfileScreenActionViewSet
from rest_framework.routers import DefaultRouter
from app.profile.views.profile_views import ProfileViewSet

router = DefaultRouter()
router.register('/profile', ProfileViewSet, basename='profile')
router.register('/profile-screen_action', ProfileScreenActionViewSet, basename='profile-screen_action')

urlpatterns = router.urls