from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from categories.views import CategoryViewSet
from credentials.views import CredentialViewSet
from transactions.views import TransactionViewSet
from users.views import UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('credentials', CredentialViewSet, basename='credential')
router.register('transactions', TransactionViewSet, basename='transaction')
router.register('users', UserViewSet, basename='user')
router.register('groups', GroupViewSet, basename='group')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
