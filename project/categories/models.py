from django.conf import settings
from django.core.exceptions import FieldError
from django.db import models


models.CharField.register_lookup(models.functions.Length)

class Category(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)

    class Meta:
        constraints = (
            models.CheckConstraint(check=models.Q(name__length__gt=0), name='length_category_name'),
            models.UniqueConstraint(fields=('user', 'name'), name='unique_category_name'),
        )
