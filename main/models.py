from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Investment(models.Model):
    date = models.DateField(default=timezone.now)
    investor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='investments')
    amount = models.DecimalField(decimal_places=2, max_digits=1000)
    notes = models.CharField(max_length=200, default=0, blank=True)

    def __str__(self):
        return self.investor.username