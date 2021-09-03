from rest_framework import serializers
from credentials.models import Credential

class CredentialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Credential
        fields = ['pk', 'user_id', 'name', 'token']
