from rest_framework.routers import DefaultRouter
from app.entrepreneurcourses.views import EntrepreneurCoursesViewSet

router = DefaultRouter()
router.register('/curso_emprendedor', EntrepreneurCoursesViewSet, basename='curso_emnprendedor')

urlpatterns = router.urls