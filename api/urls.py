from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import ReservaViewSet, PetshopModelViewSet, CategoriaModelViewSet

app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register('reservas', ReservaViewSet, basename='reservas')
router.register('petshop', PetshopModelViewSet, basename='petshop')
router.register('categoria', CategoriaModelViewSet, basename='categoria')

urlpatterns = []
urlpatterns += router.urls