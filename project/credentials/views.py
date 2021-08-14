from rest_framework import viewsets
from rest_framework import permissions
from credentials.models import Credential
from credentials.serializers import CredentialSerializer


class CredentialViewSet(viewsets.ModelViewSet):
    """API endpoint to add/edit credentials"""
    serializer_class = CredentialSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.credential_set.all()
