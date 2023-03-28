from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from signIn import views



def homepage(request):
    views.loggedIn = 0
    return render(request, 'studenthub/main.html')



