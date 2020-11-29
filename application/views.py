from django.shortcuts import render
from .forms import menuForm, requestMealForm
#from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login, authenticate
#from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone

#=======================================================
def sudo_check(user):
    if user.is_active and user.is_superuser:
        return True
    else:
        return False
 #=======================================================
@login_required
@user_passes_test(sudo_check)       
def create_menu(request):
    new_form = menuForm()
    if request.method == 'POST':
        filled_form = menuForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = 'A new menu has been created.'
        else:
            note = 'There are missing required fields'
        return render(
            request,
            'menu.html',
            {
                'menuform': new_form,
                'note': note,
            }
        )   
    else:
        return render(
            request, 
            'menu.html', 
            {
                'menuform' : new_form,
                'note': 'Hi there'
            }
        )
#=======================================================
@login_required
@user_passes_test(sudo_check)
def main_page(request):
    date = timezone.localdate()
    return render(
        request, 
        'index.html', 
        {
            'date': date,
        }
    )
#=======================================================
def appoint_meal(request):
    new_form = requestMealForm()
    if request.method == 'POST':
        filled_form = requestMealForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = (
                'Your today\'s meal has been saved!'
            )
        else:
            note = 'Are you missing something?'
        return render(
            request,
            'appoint.html',
            {
                'requestMealForm': new_form,
                'note': note,
            }

        )
    else:
        note = 'Do you already know what you wanna eat?'
        return render(
            request, 
            'appoint.html',
            {
                'requestMealForm': new_form,
                'note': note,     
            }
        )
#=======================================================


