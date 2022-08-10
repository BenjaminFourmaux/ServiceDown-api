from django.db import models
from api.models import Country, Service


class Report(models.Model):
    objects = models.Manager()

    class Meta:
        db_table = 'report'

    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    submittedAt = models.DateTimeField(auto_now_add=True)
