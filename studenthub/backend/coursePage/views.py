
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from signIn import views as signInViews
from stuhub.models import Course
from stuhub.forms import CommentForm
from django.contrib import messages


from searchPage import views as searchPageViews

def coursePage(request):
    submitted = False
    authentication = signInViews.Authenticate()
    print(authentication)
    if authentication == 1:

        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/coursePage?submitted=True')
        else:
            form = CommentForm
            if 'submitted' in request.GET:
                submitted = True
            courseList = Course.objects.all()
            for courseReq in courseList:
                if courseReq.courseName.lower() == searchPageViews.course.lower():
                # for courseee in courseReq.courseProfessors.all:
                    #    print(courseee.CourseProfessors)
                    return render(request, 'coursePage/coursePage.html', {'courseName' : courseReq.courseName.upper(),
                    'courseProfessors': courseReq.courseProfessors,
                    'courseSummary': courseReq.courseSummary,
                    'courseTutors': courseReq.courseTutors,
                    'courseComments': courseReq.courseComments,
                    'form':form,
                    'submitted':submitted})
       
    else:
       return redirect('http://127.0.0.1:8000/signIn')



