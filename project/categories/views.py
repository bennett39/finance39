from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CategorySerializer
from .models import Category


class CategoryViewSet(viewsets.ModelViewSet):
    """API endpoint to add/edit categories"""
    queryset = Category.objects.all().order_by('pk')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
