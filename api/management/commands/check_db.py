# check_db.py
import socket
import time
from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    help = "Check if port is open, avoid docker-compose race condition"

    def add_arguments(self, parser):
        parser.add_argument('service_name', help="Name of BD service")
        parser.add_argument('ip', help="IP address of DB or Docker name")
        parser.add_argument('port', help="Port numbers of BD")

    def handle(self, *args, **options):
        """ Check if port is open, avoid docker-compose race condition """

        self.stdout.write('Check Database connection')

        service_name = options['service_name']
        ip = options['ip']
        port = int(options['port'])

        # Infinite loop
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print("{0} port is open! Bye!".format(service_name))
                break
            else:
                print("{0} port is not open! I'll check it soon!".format(service_name))
                time.sleep(3)
