from django.urls import include, path
from rest_framework import routers
from credentials import views

router = routers.DefaultRouter()
router.register('credentials', views.CredentialViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
