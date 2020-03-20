from django.urls import path, include
from rest_framework.routers import DefaultRouter
from fileapi import views

router = DefaultRouter()
router.register(r'files', views.FileModelViewSet, basename="Files")

urlpatterns = [
    path('', include(router.urls))
]