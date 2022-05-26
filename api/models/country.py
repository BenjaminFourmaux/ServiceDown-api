from django.db import models
from django.db.models import Q


class Country(models.Model):
    objects = models.Manager()

    class Meta:
        db_table = 'country'

    name = models.CharField(max_length=50, null=False)
    shortname = models.CharField(max_length=2, null=True)  # ISO 3166 Alpha-2 code
    domainSuffix = models.CharField(max_length=10, null=True)

    @property
    def service_count(self):
        from api.models import Service
        return len(Service.objects.filter(Q(countries=self)))

    def __str__(self):
        return "%s - %s - %s" % (self.name, self.shortname, self.domainSuffix)
