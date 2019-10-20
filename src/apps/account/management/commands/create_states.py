from django.core.management.base import BaseCommand
from apps.account.models import State
from apps.state_choices import STATES


class Command(BaseCommand):
    help = 'Create states'

    def handle(self, *args, **options):
        result = []

        for state_name in STATES:
            state = State(name=state_name[1])
            result.append(state)

        State.objects.bulk_create(result)
