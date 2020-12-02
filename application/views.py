from django.shortcuts import render, redirect
from .models import menu, lunch
from .forms import menuForm, lunchForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.timezone import localtime, localdate
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
    :return: the rendered HTML menu form
    '''
    new_form = menuForm()
    if request.method == 'POST':
        form = menuForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data.get('date')
            if menu.objects.filter(date=date).exists():
                note = 'This date is already in use'
                return render(
                    request,
                    'createMenu.html',
                    {
                        'menuform':form,
                        'note':note
                    }
                )  
            form.save()
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
                    'menuform': form,
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
def request_lunch(request):
    '''A view to let employees to order
    their today's preferred meal and customize it.
    The form is available if Nora (or any other admin)
    already has filled 'today's' menu and if the page
    is visited before 11 AM CLT.

    :param request: the request object callout
    :return: the menu rendered HTML form
    '''
    #Check if employee already requested once a day
    date = localdate()
    if lunch.objects.filter(user=request.user, date=date).exists():
        return render(
            request,
            'requestMenu.html',
            {
                'note': 'We\'re preparing your meal!'
            }
        )
    # Check if today's menu is available
    item = menu.objects.filter(date=date)
    if item.exists() and localtime().hour < 22:
        user = lunch(user=request.user)
        new_form = lunchForm()
        if request.method == 'POST':
            form = lunchForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                note = (
                    'Your today\'s meal has been saved!'
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
    else:
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
    # Fill the form with current data
    note = ''
    pk = menu.objects.get(id=id)
    edit_form = menuForm(instance=pk)
    if request.method == 'POST':
        form = menuForm(request.POST, instance=pk)
        if form.is_valid():
            note = 'The menu has been updated' 
            form.save()
            edit_form = form
            return render(
                request, 
                'editMenu.html', 
                {
                    'form': None,
                    'note': note,
                }
            )
        else:
            note = 'Date cannot be in the past'
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
    '''A view that renders the list of requested
    lunches for 'today'.
    
    :param request: the request callout object
    :return: the rendered HTML list of requests
    '''
    orders = {}
    instant = localdate()
    for item in lunch.objects.filter(date=instant):
        orders[item.pk] = {
            'option': item.option,
            'user': item.user.username,
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
def check_details(request, id):
    '''A view dedicated to show the details
    of the requested lunch for a specific employee.

    :param request: the request callout object
    :param id: the id of the luch 
    :return: the rendered HTML list of details
    '''
    item = lunch.objects.filter(id=id)
    return render(
        request,
        'checkDetails.html',
        {
            'lunch': item,
            'pk': id,
        }
    )
#=======================================================
def show_menu(request):
    '''The main view for employees

    '''
    date = localdate()
    Menu = menu.objects.filter(date=date)
    return render(
        request,
        'showMenu.html',
        {
            'lunch': Menu,
        }
    )
#=======================================================
