from django.db import models

from django_cryptography.fields import encrypt


class Credential(models.Model):
    token = encrypt(models.CharField(max_length=255))
    name = models.CharField(max_length=120)
