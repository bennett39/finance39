from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('categories/', include('categories.urls')),
    path('credentials/', include('credentials.urls')),
    path('transactions/', include('transactions.urls')),
    path('users/', include('users.urls')),
]
