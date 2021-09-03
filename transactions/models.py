import uuid
from django.conf import settings
from django.db import models


class Transaction(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=255)
    category = models.ForeignKey('categories.Category', on_delete=models.PROTECT, null=True, blank=True)
