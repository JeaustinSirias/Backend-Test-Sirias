from django import forms
from .models import menu, employee


class menuForm(forms.ModelForm):
    '''The form for the menu model'''

    class Meta:
        model = menu
        fields = '__all__'
        labels = {
            'meal_one': 'Option 1',
            'meal_two': 'Option 2',
            'meal_three': 'Option 3',
            'meal_four': 'Option 4',  
            'date': 'Date'        
        }
        help_texts = {
            'date': 'Format MM/DD/YYYY',
        }

class requestMealForm(forms.ModelForm):
    '''The form for employees to fill their 
    preferred day's meal'''

    class Meta:
        model = employee
        fields = '__all__'
        labels = {
            'prefered_meal': 'Choose your preferred meal',
            'custom_preference': 'Any custom preference?',
        }