from django.http import HttpResponse
from django.shortcuts import render,redirect


from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from .forms import CreateUserForm
from signIn import views

def register(request):
    views.loggedIn = 0
    form = form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        user = form.cleaned_data.get('first_name')
        messages.success(request, 'Account successfully created for ' + user )
        

    context = {'form': form}
    #return HttpResponse("about")
    return render(request, 'register/register.html',context)
