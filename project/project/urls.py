from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from categories.views import CategoryViewSet
from credentials.views import CredentialViewSet
from transactions.views import TransactionViewSet
from users.views import UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('credentials', CredentialViewSet)
router.register('transactions', TransactionViewSet)
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
