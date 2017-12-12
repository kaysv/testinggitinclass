from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def FrontPageView(request):
    return render(request, 'login/home.html', {})



# this handles login
def LoginView(request):
    # Checking reququest
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get('password')

        #Lets authenticate user
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return HttpResponse("success")
        else:
            return HttpResponse("error")
    return redirect("/")


# this perfforms logout
def LogoutView(request):
    logout(request)
    return redirect("/")
