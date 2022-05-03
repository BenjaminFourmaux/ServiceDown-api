from django.db import models


class Test(models.Model):
    object = []

    class Meta:
        db_table = 'test'

    label = models.CharField(max_length=255, null=True)
