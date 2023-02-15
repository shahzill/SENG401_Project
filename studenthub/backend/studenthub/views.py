from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    #return HttpResponse("about")
    return render(request, 'studenthub\main.html')

