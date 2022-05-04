from django.db import models


class Country(models.Model):
    class Meta:
        db_table = 'country'

    name = models.CharField(max_length=50, null=False)
    shortname = models.CharField(max_length=2, null=True)  # ISO 3166 Alpha-2 code
    domainSuffix = models.CharField(max_length=10, null=True)

    def __str__(self):
        return "%s - %s - %s" % (self.name, self.shortname, self.domainSuffix)
