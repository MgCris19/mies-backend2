from rest_framework.routers import DefaultRouter
from app.academic.views import TrainerViewSet, FacultyViewSet, TrainerCategoryViewSet, CareerViewSet, StudentViewSet

router = DefaultRouter()
router.register('/capacitador', TrainerViewSet, basename='capacitador')
router.register('/facultad', FacultyViewSet,basename='facultad')
router.register('/categoria_capacitador', TrainerCategoryViewSet,basename='categoria_capacitador')
router.register('/carrera', CareerViewSet,basename='carrera')
router.register('/estudiante', StudentViewSet, basename='estudiante')

urlpatterns = router.urls
