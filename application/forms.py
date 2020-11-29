from django import forms
from .models import menu, employee


class menuForm(forms.ModelForm):
    '''The form for the menu model'''

    class Meta:
        model = menu
        fields = '__all__'
        labels = {
            'meal_one': 'First meal option',
            'meal_two': 'Second meal option',
            'meal_three': 'Third meal option',
            'meal_four': 'Fourth meal option',  
            'date': 'Date'        
        }

class requestMealForm(forms.ModelForm):
    '''The form for employees to fill their 
    preferred day's meal'''

    class Meta:
        model = employee
        fields = [
            'prefered_meal',
            'custom_preference',
        ]
        labels = {
            'prefered_meal': 'Choose your preferred meal',
            'custom_preference': 'Any custom preference?',
        }