import uuid
from django.conf import settings
from django.db import models

from django_cryptography.fields import encrypt


models.CharField.register_lookup(models.functions.Length)

class Credential(models.Model):
    PLAID_CLIENT_ID = 'PLAID_CLIENT_ID'
    PLAID_CLIENT_SECRET = 'PLAID_CLIENT_SECRET'
    PLAID_PUBLIC_KEY = 'PLAID_PUBLIC_KEY'
    PLAID_TOKEN = 'PLAID_TOKEN'
    TOKEN_TYPES = (
        (PLAID_CLIENT_ID, 'Plaid Client ID'),
        (PLAID_CLIENT_SECRET, 'Plaid Client Secret'),
        (PLAID_PUBLIC_KEY, 'Plaid Public Key'),
        (PLAID_TOKEN, 'Plaid Token'),
    )

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    token = encrypt(models.CharField(max_length=255))
    name = models.CharField(max_length=120)
    token_type = models.CharField(max_length=50, choices=TOKEN_TYPES)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        constraints = (
            models.CheckConstraint(check=models.Q(name__length__gt=0), name='length_credential_name'),
            models.CheckConstraint(check=models.Q(token_type__length__gt=0), name='length_credential_tokentype'),
            models.UniqueConstraint(fields=('user', 'token'), name='unique_credential_token'),
            models.UniqueConstraint(fields=('user', 'name'), name='unique_credential_name'),
        )
