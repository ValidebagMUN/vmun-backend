from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .settings import DEBUG, ADMIN_URL
from . import views

if DEBUG:
    router = routers.DefaultRouter()
else:
    router = routers.SimpleRouter()

router.register(r'users', views.UserViewSet)

urlpatterns = [
    path(ADMIN_URL, admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'auth/', include('djoser.urls')),
    path(r'auth/', include('djoser.urls.authtoken')),

]
