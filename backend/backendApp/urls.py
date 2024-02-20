from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NameViewSet, ScoreViewSet

router = DefaultRouter()
router.register('names', NameViewSet)
router.register('scores', ScoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
]