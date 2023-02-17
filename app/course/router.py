from rest_framework.routers import DefaultRouter
from app.course.views import CourseCategoryViewSet, CourseViewSet, LocalityCoursesViewSet, CourseTrainerViewSet


router = DefaultRouter()
router.register('/curso', CourseViewSet, basename='curso')
router.register('/categoria_curso', CourseCategoryViewSet,basename='categoria_curso')
router.register('/curso_localidad', LocalityCoursesViewSet,basename='curso_localidad')
router.register('/curso_capacitador', CourseTrainerViewSet,basename='curso_capacitador')

urlpatterns = router.urls
