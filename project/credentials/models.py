from django.conf import settings
from django.db import models

from django_cryptography.fields import encrypt


models.CharField.register_lookup(models.functions.Length)

class Credential(models.Model):
    token = encrypt(models.CharField(max_length=255))
    name = models.CharField(max_length=120)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        constraints = (
            models.CheckConstraint(check=models.Q(name__length__gt=0), name='length_credential_name'),
            models.UniqueConstraint(fields=('user', 'token'), name='unique_credential_token'),
            models.UniqueConstraint(fields=('user', 'name'), name='unique_credential_name'),
        )
