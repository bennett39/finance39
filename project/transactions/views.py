from rest_framework import viewsets
from rest_framework import permissions
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    """API endpoint to add/edit transactions"""
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
