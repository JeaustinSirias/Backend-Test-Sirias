from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import localdate
from django.core.exceptions import ValidationError

#=====================================================
def validate_date(date):
    if date < localdate():
        raise ValidationError(
            ('Wrong'), code='invalid'
        )

class menu(models.Model):
    '''The menu model with its respective
    four meals entries'''
    meal_one = models.CharField(max_length=255)
    meal_two = models.CharField(max_length=255)
    meal_three = models.CharField(max_length=255)
    meal_four = models.CharField(max_length=255)
    date = models.DateField(
        null=True, 
        blank=True, 
        default=None, 
        validators=[validate_date],
    )

class employee(models.Model):
    MENU = [
        ('Option 1', 'Option 1'),
        ('Option 2', 'Option 2'),
        ('Option 3', 'Option 3'),
        ('Option 4', 'Option 4'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    option = models.CharField(max_length=255, choices=MENU)
    preference = models.CharField(max_length=40)
    date = models.DateField(default=localdate, editable=False)




