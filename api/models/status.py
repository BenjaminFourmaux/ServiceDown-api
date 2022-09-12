from django.db import models
from enum import Enum


class Status(models.Model):
    objects = models.Manager()

    class Meta:
        db_table = 'status'

    label = models.CharField(max_length=10, null=False)


class StatusEnum(Enum):
    OK = "ok",
    WARNING = "warning",
    ERROR = "error",
