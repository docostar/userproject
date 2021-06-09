from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login

# Create your views here.

def index(request):
    print(request.method)
    if request.user.is_authenticated:
        return render(request,"index.html")
    return redirect("/login")


def loginUser(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password = request.POST.get('password')
        #check user enter correct credancial or not
        user = authenticate(username=username, password=password)
        if user is not None:
        # A backend authenticated the credential
            login(request,user)
            return redirect("/")
        else:
            return render(request, "login.html")
    # No backend authenticated the credentials
    return render(request,"login.html")

def logoutUser(request):
    logout(request)
    return redirect("/login")