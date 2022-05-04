from django.db import models
from api.models.country import Country


class Service(models.Model):
    class Meta:
        db_table = 'service'

    name = models.CharField(max_length=255, null=False)
    cname = models.CharField(max_length=255, null=False)
    description = models.TextField(max_length=300, null=True)
    path = models.URLField(max_length=100, null=False)
    countries = models.ManyToManyField(Country)

    def __str__(self):
        return "%s - %s" % (self.name, self.cname)
