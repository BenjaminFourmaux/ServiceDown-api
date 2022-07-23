import time
from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    help = "DEV COMMAND: Fill database with a set of data for testing purposes"

    def handle(self, *args, **options):
        list_fixtures = ['countries', 'services']

        self.stdout.write('Load Fixtures ...')
        for i in range(len(list_fixtures)):
            time.sleep(1)
            self.progressBar(i, len(list_fixtures))

            call_command('loaddata', list_fixtures[i] + '.json', verbosity=0)

        self.progressBar(len(list_fixtures), len(list_fixtures))
        self.stdout.write(self.style.ERROR('Fixtures Applied'))

    def progressBar(self, count, total, suffix=''):
        """
            src : https://twitter.com/clcoding/status/1549819582390894592/photo/1
        """
        bar_length = 60
        filled_length = int(round(bar_length * count / float(total)))

        percent = round(100.0 * count / float(total), 1)
        bar = '=' * filled_length + '>' + '-' * (bar_length - filled_length)

        self.stdout.write('[%s] %s%s %s\r' % (bar, percent, '%', suffix))
        self.stdout.flush()
