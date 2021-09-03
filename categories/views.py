from rest_framework import viewsets
from rest_framework import permissions
from categories.serializers import CategorySerializer
from categories.models import Category


class CategoryViewSet(viewsets.ModelViewSet):
    """API endpoint to add/edit categories"""
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.category_set.all()
