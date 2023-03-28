
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from signIn import views as signInViews
from stuhub.models import Course

from django.contrib import messages
from .forms import applyTutorForm
from django.contrib import messages



from searchPage import views as searchPageViews

def tutorPage(request, name, id):
    
    authentication = signInViews.Authenticate()
    print(authentication)
    if authentication == 1:
        courseList = Course.objects.all()
        for courseReq in courseList:
            if courseReq.courseName.lower() == searchPageViews.course.lower():
                for tutor in (courseReq.courseTutors).all():
                    if tutor.tutorName == name:
                        if tutor.tutorID == id:
                            return render(request, 'tutorPage/tutorPage.html', {
                            'courseTutors': tutor})
       
    else:
       return redirect('http://127.0.0.1:8000/signIn')




def becomeTutorPage(request):
    form = applyTutorForm()
    if request.method == 'POST':
        form = applyTutorForm(request.POST)
        if form.is_valid():
            
            form.save()
            messages.info(request, 'Your application has been submitted!')
            return redirect('http://127.0.0.1:8000/tutorPage/becomeTutorPage/')
    
    return render(request, 'becomeTutorPage/becomeTutor.html', {'form':form})