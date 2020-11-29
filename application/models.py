from django.db import models
from django.utils.timezone import localdate
from django.core.exceptions import ValidationError

def validate_date(date):
    if date < localdate():
        raise ValidationError(
            ('Date cannot be in the past'), code='invalid'
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
    prefered_meal = models.CharField(max_length=255)
    custom_preference = models.CharField(max_length=255)
    #name = models.CharField(max_length=50)
    #phone = models.CharField(maxlength=10)



