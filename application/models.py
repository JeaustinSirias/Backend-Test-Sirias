from django.db import models

class menu(models.Model):
    '''The menu model with its respective
    entries'''

    meal_one = models.CharField(max_length=255)
    meal_two = models.CharField(max_length=255)
    meal_three = models.CharField(max_length=255)
    meal_four = models.CharField(max_length=255)



