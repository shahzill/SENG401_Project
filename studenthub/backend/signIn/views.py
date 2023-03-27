from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def signIn(request):
    global loggedIn
    loggedIn = 0
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            loggedIn = 1
            return redirect('http://127.0.0.1:8000/searchPage')
        else:
            messages.info(request, 'Username or Password incorrect')

    #return HttpResponse("about")
    return render(request, 'signIn/signIn.html')

def Authenticate():
    return loggedIn