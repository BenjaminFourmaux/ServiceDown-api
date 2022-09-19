from django.db import models
from api.models import Service, Country, Status


class CurrentStatus(models.Model):
    class Meta:
        db_table = 'current_state'

    objects = models.Manager()

    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, default=1, on_delete=models.DO_NOTHING)
