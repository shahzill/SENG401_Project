
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from signIn import views as signInViews
from stuhub.models import Course
from stuhub.models import Comment
from stuhub.forms import CommentForm
from django.contrib import messages


from searchPage import views as searchPageViews

def coursePage(request):
    submitted = False
    authentication = signInViews.Authenticate()
    print(authentication)
    if authentication == 1:

        if request.method == "POST":
            profRating = request.POST.get("ProfRating")
            prof = request.POST.get("ProfName")
            courseComments = request.POST.get("Comment")
            commenterName = request.POST.get("CommenterName")
            com = Comment.objects.create(
                courseName=searchPageViews.course.upper(),
                professorRating = profRating,
                professorN = prof,
                courseComment = courseComments,
                commenterName = commenterName

            )       
            return HttpResponseRedirect('/coursePage?submitted=True')
        else:
            form = CommentForm
            if 'submitted' in request.GET:
                submitted = True
            courseList = Course.objects.all()
            commentList = Comment.objects.all()
            coursecom =[]
            for courseReq in courseList:
                if courseReq.courseName.lower() == searchPageViews.course.lower():
                    for commentReq in commentList:
                        if commentReq.courseName.lower() == searchPageViews.course.lower():
                            coursecom.append(commentReq)
                
                    return render(request, 'coursePage/coursePage.html', {'courseName' : courseReq.courseName.upper(),
                    'courseProfessors': courseReq.courseProfessors,
                    'courseSummary': courseReq.courseSummary,
                    'courseTutors': courseReq.courseTutors,
                    'form':form,
                    'submitted':submitted,
                    'allComments': coursecom})
       
    else:
       return redirect('http://127.0.0.1:8000/signIn')


def add_comment(request):
    if request.method == "POST":
        profRating = request.POST.get("ProfRating")
        prof = request.POST.get("ProfName")
        courseComments = request.POST.get("Comment")
        commenterName = request.POST.get("CommenterName")
        com = Comment.objects.create(
            courseName='ENGG200',
            professorRating = profRating,
            professorN = prof,
            courseComment = courseComments,
            commenterName = commenterName

        )

def coursePageLink(request,course):
    searchPageViews.course = course
    submitted = False
    authentication = signInViews.Authenticate()
    print(authentication)
    if authentication == 1:
        form = CommentForm
        if 'submitted' in request.GET:
            submitted = True
        courseList = Course.objects.all()
        commentList = Comment.objects.all()
        coursecom = []
        for courseReq in courseList:
            if courseReq.courseName.lower() == course.lower():
                
                return render(request, 'coursePage/coursePage.html', {'courseName' : courseReq.courseName.upper(),
                    'courseProfessors': courseReq.courseProfessors,
                    'courseSummary': courseReq.courseSummary,
                    'courseTutors': courseReq.courseTutors,
                    'form':form,
                    'submitted':submitted,
                    'allComments': coursecom})
    else:
        return redirect('http://127.0.0.1:8000/signIn')
