from rest_framework import viewsets
from rest_framework import permissions
from .models import Credential
from .serializers import CredentialSerializer


class CredentialViewSet(viewsets.ModelViewSet):
    """API endpoint to add/edit credentials"""
    queryset = Credential.objects.all()
    serializer_class = CredentialSerializer
    permission_classes = [permissions.IsAuthenticated]
