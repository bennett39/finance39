from django.conf import settings
from django.db import models

class Category(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)

    class Meta:
        unique_together = ('user', 'name',)
