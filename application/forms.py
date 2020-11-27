from django import forms
from .models import menu


class menu_form(forms.ModelForm):
    '''The form for the menu model'''

    class Meta:
        model = menu
        fields = [
            'meal_one',
            'meal_two',
            'meal_three',
            'meal_four',
        ]
        labels = {
            'meal_one': 'First meal option',
            'meal_two': 'Second meal option',
            'meal_three': 'Third meal option',
            'meal_four': 'Fourth meal option',          
        }