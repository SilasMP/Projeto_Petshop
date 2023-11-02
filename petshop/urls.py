from django.contrib import admin
from django.urls import path, include
from base.views import *
from reserva.views import reserva


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/login/', admin_login, name='admin-login'),
    path('', home, name='home'),
    path('contato', contato, name='contato'),
    path('reserva', reserva, name='reserva'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls', namespace='api')),
]
