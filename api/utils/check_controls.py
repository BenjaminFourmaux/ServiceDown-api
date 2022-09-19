from api.models import Country, Service
from api.utils import CountryNotFound, CountryNotAvailable, ServiceNotFound, ServiceNotInCountry


class CheckControlsUtils:

    @staticmethod
    def check_country(country_id) -> Country:
        try:
            country = Country.objects.get(pk=country_id)
        except:
            raise CountryNotFound
        if not country.isAvailable:
            raise CountryNotAvailable
        return country

    @staticmethod
    def check_service(service_id) -> Service:
        try:
            service = Service.objects.get(pk=service_id)
        except:
            raise ServiceNotFound
        return service

    @classmethod
    def check_service_country(cls, service_id, country_id):
        service = cls.check_service(service_id)
        country = cls.check_country(country_id)

        if country not in service.countries.all():
            raise ServiceNotInCountry
