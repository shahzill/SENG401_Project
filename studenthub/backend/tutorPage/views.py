
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from signIn import views as signInViews
from stuhub.models import Course

from django.contrib import messages

from .forms import CreateUserForm

from searchPage import views as searchPageViews

def tutorPage(request):
    
    authentication = signInViews.Authenticate()
    print(authentication)
    if authentication == 1:
        
        return render(request, 'tutorPage/tutorPage.html')
       
    else:
       return redirect('http://127.0.0.1:8000/signIn')



