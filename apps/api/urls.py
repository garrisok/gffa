from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'people', views.PersonViewSet)
router.register(r'planets', views.PlanetViewSet)
router.register(r'vehicles', views.PlanetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]