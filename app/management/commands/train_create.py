from django.core.management.base import BaseCommand
from line.einstein_vision import Train
from line.service import json_dumps


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        self.train = Train()
        super(Command, self).__init__(*args, **kwargs)

    def add_arguments(self, parser):
        parser.add_argument('--datasets_id',
                            dest='datasets_id', nargs='?', type=str)
        parser.add_argument('--name',
                            dest='name', nargs='?', type=str)

    def handle(self, *args, **options):
        datasets_id = options.get('datasets_id')
        name = options.get('name')
        result = self.train.create(
            datasets_id=datasets_id, name=name)
        print(json_dumps(result))
