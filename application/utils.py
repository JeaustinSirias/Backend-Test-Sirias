import uuid
from django.utils.timezone import localdate
from django.core.exceptions import ValidationError

def spawn_uuid():
    '''Generates a random
    UUID key'''
    return uuid.uuid4().hex

def validate_date(date):
    if date < localdate():
        raise ValidationError(
            ('Wrong'), code='invalid'
        )

