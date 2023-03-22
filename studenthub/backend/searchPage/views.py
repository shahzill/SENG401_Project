
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from signIn import views
from stuhub.models import Course

from django.contrib import messages

from .forms import CreateUserForm



def searchPage(request):
    print("NAYYYY")
    authentication = views.Authenticate()
    print(authentication)
    courseList = Course.objects.all()
    global course 
    course = None
    global reqMethod
    reqMethod = request.method
    if request.method == 'POST':
        
        course = request.POST.get('course')
        for courseReq in courseList:
            if courseReq.courseName.lower() == course.lower():
              return redirect('http://127.0.0.1:8000/coursePage')  

          
        
    else:
        print("NOOOO")
    if authentication == 1:
        return render(request, 'searchPage/searchPage.html', {'courseList': courseList})
    else:
       return redirect('http://127.0.0.1:8000/signIn')



    
    
        
    
