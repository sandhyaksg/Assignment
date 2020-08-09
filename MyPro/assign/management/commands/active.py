from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from assign.factories import activityPeriodsFactory
class Command(BaseCommand):
    help = 'Create random activityPeriods'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of activityPeriods')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            activityPeriodsFactory.create()