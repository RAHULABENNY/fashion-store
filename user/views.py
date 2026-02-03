from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from menu.models import Clothitems


# Create your views here.
def home(request):
    # Fetch only available items for the home page
    items = Clothitems.objects.filter(is_avilable=True) 
    
    # You MUST pass the items in a dictionary as the third argument
    return render(request, 'home.html', {'items': items})




def login_view(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'invalid username or password')
            return redirect('login')
    return render(request,'login.html')


def signup_view(request):
    if request.method=="POST":
        username=request.POST.get("username")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")
        if password!=confirm_password:
            messages.error(request,"password do not match")
            return redirect('signup')
        if User.objects.filter(username=username).exists():
            messages.error(request,'user name alredy exists')
            return redirect('signup')
        user=User.objects.create_user(
            username=username,
            last_name=last_name,
            email=email,
            password=password,  
        )
        user.save()
        login(request,user)
        messages.success(request,"user created successfully")
        return redirect("home")
    return render(request,"signup.html")

