from django.urls import include, path
from rest_framework import routers
from categories import views

router = routers.DefaultRouter()
router.register('categories', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
