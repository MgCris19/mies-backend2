from rest_framework.routers import DefaultRouter
from django.urls import path, include
from app.balancedScoredCard.views import PerspectiveViewSet, IndicatorViewSet,ObjectiveViewSet,BscViewSet, ControlViewSet
from app.balancedScoredCard.apiBsc import getBscByName

router = DefaultRouter()
router.register('/perspectiva', PerspectiveViewSet, basename='perspectiva')
router.register('/indicadores', IndicatorViewSet, basename='indicadores')
router.register('/objetivos', ObjectiveViewSet, basename='objetivos')
router.register('/bsc', BscViewSet, basename='bsc')
router.register('/control', ControlViewSet, basename='control')

urlpatterns = [
    path('', include(router.urls)),
    path('/bsc/search', getBscByName),
]

