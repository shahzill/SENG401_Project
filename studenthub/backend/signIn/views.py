from django.http import HttpResponse
from django.shortcuts import render

def signIn(request):
    #return HttpResponse("about")
    return render(request, 'signIn/signIn.html')


