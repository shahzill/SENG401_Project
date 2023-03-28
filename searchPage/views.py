
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from signIn import views
from stuhub.models import Course, CourseRequest

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
    submitted = False
    if 'submitted' in request.GET:
            
            print("ICOME HERE")
    if request.method == 'POST':
        global newCourse 
        newCourse = False
        
        course = request.POST.get('course')
        
  
        for courseReq in courseList:
            if courseReq.courseName.lower() == course.lower():
              newCourse = True
              return redirect('https://uofcstudenthub.up.railway.app/coursePage') 
        
        if newCourse == False:
                submitted = True
                com = CourseRequest.objects.create(
                    courseName=course

            )
             
        
    else:
        print("NOOOO")
    if authentication == 1:
        return render(request, 'searchPage/searchPage.html', {'courseList': courseList, 'submitted':submitted})
    else:
       return redirect('https://uofcstudenthub.up.railway.app/signIn')


    
    
        
    