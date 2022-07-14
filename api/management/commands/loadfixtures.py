from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    help = "DEV COMMAND: Fill databasse with a set of data for testing purposes"

    def handle(self, *args, **options):
        list_fixtures = ['countries', 'services']

        self.stdout.write('Load Fixtures ...')
        for fixture in list_fixtures:
            call_command('loaddata', fixture + '.json', verbosity=1)
        self.stdout.write(self.style.ERROR('Fixtures Applied'))
