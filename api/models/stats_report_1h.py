from django.db import models
from api.models import Country, Service


class StatsReport1H (models.Model):
    objects = models.Manager()

    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    interval5mins = models.IntegerField(db_column='slice1')
    interval10mins = models.IntegerField(db_column='slice2')
    interval15mins = models.IntegerField(db_column='slice3')
    interval20mins = models.IntegerField(db_column='slice4')
    interval25mins = models.IntegerField(db_column='slice5')
    interval30mins = models.IntegerField(db_column='slice6')
    interval35mins = models.IntegerField(db_column='slice7')
    interval40mins = models.IntegerField(db_column='slice8')
    interval45mins = models.IntegerField(db_column='slice9')
    interval50mins = models.IntegerField(db_column='slice10')
    interval55mins = models.IntegerField(db_column='slice11')
    interval60mins = models.IntegerField(db_column='slice12')

    class Meta:
        managed = False
        db_table = 'stats_report_1h'
