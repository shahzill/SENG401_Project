
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

def profPage(request, name, id,courseName):
    
    authentication = signInViews.Authenticate()
    print(authentication)
    if authentication == 1:
        courseList = Course.objects.all()
        for courseReq in courseList:
            if searchPageViews.reqMethod == 'POST':
                if courseReq.courseName.lower() == searchPageViews.course.lower():
                    for prof in (courseReq.courseProfessors).all():
                        if prof.profName == name:
                            if prof.profID == id:
                                return render(request, 'profPage/profPage.html', {
                                'courseProfessors': prof})
            else:

                if courseReq.courseName.lower() == courseName.lower():
                    for prof in (courseReq.courseProfessors).all():
                        if prof.profName == name:
                            if prof.profID == id:
                                return render(request, 'profPage/profPage.html', {
                                'courseProfessors': prof})
            
            # if  or courseReq.courseName.lower() == courseName.lower():
                
       
    else:
       return redirect('https://uofcstudenthub.up.railway.app/signIn')