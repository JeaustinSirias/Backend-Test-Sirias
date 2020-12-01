from django.shortcuts import render, redirect
from .models import menu, employee
from .forms import menuForm, requestMealForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.timezone import localtime, localdate, now, timedelta

#=======================================================
def sudo_check(user):
    '''A method to checkout if an user 
    has 'superuser' privileges

    :param user: the current authenticated user
    :return: boolean
    '''
    if user.is_active and user.is_superuser:
        return True
    else:
        return False
 #=======================================================
@login_required
@user_passes_test(sudo_check)       
def create_menu(request):
    '''A view that renders a form to create a menu
    for a specific date.

    :param request: the request callout object
    :return: the rendered menu HTML form
    '''
    new_form = menuForm()
    if request.method == 'POST':
        filled_form = menuForm(request.POST)
        if filled_form.is_valid():
            date = filled_form.cleaned_data.get('date')
            for instant in menu.objects.all():
                if date == instant.date:
                    note = 'This date is already in use'
                    return render(
                        request,
                        'createMenu.html',
                        {
                            'menuform':filled_form,
                            'note':note
                        }
                    )  
            filled_form.save()
            note = 'A new menu has been created'
            return render(
                request,
                'createMenu.html',
                {   
                    'menuform': None,
                    'note': note,
                }
            )             
        else:
            note = 'Date cannot be in the past'
            return render(
                request,
                'createMenu.html',
                {
                    'menuform': filled_form,
                    'note': note,
                }
            )  
    else:
        return render(
            request, 
            'createMenu.html', 
            {
                'menuform' : new_form,
                #'note': ''
            }
        )
#=======================================================
@login_required
@user_passes_test(sudo_check)
def main_page(request):
    '''The admin's (Nora) mainpage view.

    :param request: the request callout object
    :return: the homepage rendered HTML temp.
    '''
    date = localtime()
    return render(
        request, 
        'index.html', 
        {
            'date': date,
        }
    )
#=======================================================
@login_required
def request_menu(request):
    '''A view to let employees to order
    their today's preferred meal and customize it.
    The form is available if Nora (or any other admin)
    already has filled 'today's' menu and if the page
    is visited before 11 AM CLT.

    :param request: the request object callout
    :return: the menu rendered HTML form
    '''
    #Check if employee already requested once a day
    '''
    delta = now() - timedelta(days=1)
    if employee.objects.filter(user=request.user, date=delta).exists():
        return render(
            request,
            'requestMenu.html',
            {
                'note': 'You already requested your meal'
            }
        )
    '''
    # Check if today's menu is available
    today = localtime()
    instant = localdate()
    item = menu.objects.filter(date=today)
    if today.hour < 22:
        user = employee(user=request.user)
        new_form = requestMealForm(instance=user)
        if request.method == 'POST':
            form = requestMealForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                note = (
                    'Your today\'s meal has been saved!'
                )
            else:
                note = 'Are you missing something?'
            return render(
                request,
                'requestMenu.html',
                {
                    'requestMealForm': new_form,
                    'note': note,
                }
            )
        else:
            note = 'So what are you gonna eat?'
            return render(
                request, 
                'requestMenu.html',
                {
                    'requestMealForm': new_form,
                    'note': note,
                    'todays_menu': item,     
                }
            )
    note = 'Today\'s menu is not available'
    return render(
        request, 
        'requestMenu.html',
        {
            'requestMealForm': None,
            'note': note,     
        }
    )
#=======================================================
@login_required
@user_passes_test(sudo_check)
def list_menu(request):
    '''An iterative method to show all the listed
    menus in the database.

    :param request: the request call object
    :return: the menu rendered HTML list
    '''    
    menu_dict = {}
    for obj in menu.objects.all():
        menu_dict[obj.pk] = {
            'date': obj.date,
        }
    return render(
        request,
        'listMenu.html',
        {
            'menu_list': menu_dict,
        }
    )
#=======================================================
@login_required
@user_passes_test(sudo_check)
def edit_menu(request, id):
    '''A method to update or modify a menu.

    :param request: the request call object
    :param id: the primary key of the menu to modify
    :return: the rendered menu HTML update form
    '''
    note = ''
    primary_key = menu.objects.get(id=id)
    edit_form = menuForm(instance=primary_key)
    if request.method == 'POST':
        form = menuForm(
            data=request.POST, 
            instance=primary_key
        )
        if form.is_valid():
            date = form.cleaned_data.get('date')
            for item in menu.objects.all():
                if date == item.date:
                    note = 'This date is already in use'
                    return render(
                        request,
                        'editMenu.html',
                        {
                            'form': form,
                            'note': note,
                        }
                    )
            note = 'The %s menu has been updated' %date    
            form.save()
            edit_form = form
            return render(
                request, 
                'editMenu.html', 
                {
                    'note': note,
                }
            )
        else:
            note = 'Invalid date format. Try again.'
            return render(
                request, 
                'editMenu.html', 
                {
                    'form': form,
                    'note': note,
                }
            )
    return render(
        request, 
        'editMenu.html', 
        {
            'form': edit_form,
            'note': note,
        }
    )
#=======================================================
def delete_menu(request, id):
    '''A method for superusers to delete their
    linked menus in case they won't 
    need them.

    :param request: the request object callout
    :param id: the object's primary key
    :return: redirects 
    '''
    form = menu.objects.get(id=id)
    form.delete()
    return redirect(to='list')
#=======================================================
@login_required
@user_passes_test(sudo_check)
def list_requests(request):
    orders = {}
    instant = localdate()
    for item in employee.objects.filter(date=instant):
        orders[item.pk] = {
            'option': item.option,
        }
    return render(
        request,
        'listRequests.html',
        {
           'requests_list': orders,
           'date': instant,
        }
    )
#=======================================================
