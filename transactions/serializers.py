
from rest_framework import serializers
from transactions.models import Transaction

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ['pk', 'user_id', 'amount', 'date', 'description', 'category_id']
