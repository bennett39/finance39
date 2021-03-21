from django.db import models


class Transaction(models.Model):
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=255)
