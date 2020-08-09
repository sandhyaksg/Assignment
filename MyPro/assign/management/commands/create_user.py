from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from assign.factories import UserFactory
class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('active_id', nargs='+', type=int, help='Active ID')
    def handle(self, *args, **kwargs):
            UserFactory.create(activity_periods=kwargs['active_id'])