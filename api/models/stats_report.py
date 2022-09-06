from django.db import models
from api.models import Country, Service


class StatsReport1H (models.Model):
    objects = models.Manager()

    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    totalReport = models.IntegerField(db_column='totalReport')
    interval60mins = models.IntegerField(db_column='slice1')
    interval55mins = models.IntegerField(db_column='slice2')
    interval50mins = models.IntegerField(db_column='slice3')
    interval45mins = models.IntegerField(db_column='slice4')
    interval40mins = models.IntegerField(db_column='slice5')
    interval35mins = models.IntegerField(db_column='slice6')
    interval30mins = models.IntegerField(db_column='slice7')
    interval25mins = models.IntegerField(db_column='slice8')
    interval20mins = models.IntegerField(db_column='slice9')
    interval15mins = models.IntegerField(db_column='slice10')
    interval10mins = models.IntegerField(db_column='slice11')
    interval5mins = models.IntegerField(db_column='slice12')

    class Meta:
        managed = False
        db_table = 'stats_report_1h'


class StatsReport24H (models.Model):
    objects = models.Manager()

    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    totalReport = models.IntegerField(db_column='totalReport')
    interval24hours = models.IntegerField(db_column='slice1')
    interval23hours = models.IntegerField(db_column='slice2')
    interval22hours = models.IntegerField(db_column='slice3')
    interval21hours = models.IntegerField(db_column='slice4')
    interval20hours = models.IntegerField(db_column='slice5')
    interval19hours = models.IntegerField(db_column='slice6')
    interval18hours = models.IntegerField(db_column='slice7')
    interval17hours = models.IntegerField(db_column='slice8')
    interval16hours = models.IntegerField(db_column='slice9')
    interval15hours = models.IntegerField(db_column='slice10')
    interval14hours = models.IntegerField(db_column='slice11')
    interval13hours = models.IntegerField(db_column='slice12')
    interval12hours = models.IntegerField(db_column='slice13')
    interval11hours = models.IntegerField(db_column='slice14')
    interval10hours = models.IntegerField(db_column='slice15')
    interval9hours = models.IntegerField(db_column='slice16')
    interval8hours = models.IntegerField(db_column='slice17')
    interval7hours = models.IntegerField(db_column='slice18')
    interval6hours = models.IntegerField(db_column='slice19')
    interval5hours = models.IntegerField(db_column='slice20')
    interval4hours = models.IntegerField(db_column='slice21')
    interval3hours = models.IntegerField(db_column='slice22')
    interval2hours = models.IntegerField(db_column='slice23')
    interval1hours = models.IntegerField(db_column='slice24')

    class Meta:
        managed = False
        db_table = 'stats_report_24h'
