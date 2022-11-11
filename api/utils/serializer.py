from api.models import StatsReport24H, StatsReport1H
from api.utils import SerializerHasNoField


class SerializerUtils:

    @staticmethod
    def check_field_is_in_serializer(requested_fields: [], serializer_field: [], serializer_name: str):
        for field in requested_fields:
            if field not in serializer_field:
                # Raise error
                raise SerializerHasNoField([field, serializer_name])

    @staticmethod
    def emptyStats1H(stats_obj: StatsReport1H) -> StatsReport1H:
        stats_obj.interval5mins = 0
        stats_obj.interval10mins = 0
        stats_obj.interval15mins = 0
        stats_obj.interval20mins = 0
        stats_obj.interval25mins = 0
        stats_obj.interval30mins = 0
        stats_obj.interval35mins = 0
        stats_obj.interval40mins = 0
        stats_obj.interval45mins = 0
        stats_obj.interval50mins = 0
        stats_obj.interval55mins = 0
        stats_obj.interval60mins = 0
        return stats_obj

    @staticmethod
    def emptyStats24H(stats_obj: StatsReport24H) -> StatsReport24H:
        stats_obj.interval1hours = 0
        stats_obj.interval2hours = 0
        stats_obj.interval3hours = 0
        stats_obj.interval4hours = 0
        stats_obj.interval5hours = 0
        stats_obj.interval6hours = 0
        stats_obj.interval7hours = 0
        stats_obj.interval8hours = 0
        stats_obj.interval9hours = 0
        stats_obj.interval10hours = 0
        stats_obj.interval11hours = 0
        stats_obj.interval12hours = 0
        stats_obj.interval13hours = 0
        stats_obj.interval14hours = 0
        stats_obj.interval15hours = 0
        stats_obj.interval16hours = 0
        stats_obj.interval17hours = 0
        stats_obj.interval18hours = 0
        stats_obj.interval19hours = 0
        stats_obj.interval20hours = 0
        stats_obj.interval21hours = 0
        stats_obj.interval22hours = 0
        stats_obj.interval23hours = 0
        stats_obj.interval24hours = 0
        stats_obj.totalReport = 0
        return stats_obj
