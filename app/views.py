from django.shortcuts import render
from . models import *

# Create your views here.

# View for register page:

def RegisterPage(request):
    return render(request,"app/register.html")


# View for User Registration

def UserRegister(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        contact = request.POST['contact']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        # First validate the user already exist or not
        user = User.objects.filter(Email=email)        

        if user:
            message = "User already Exists"
            return render(request,"app/register.html",{'msg':message})
        else:
            if password == cpassword:
                newuser = User.objects.create(Firstname=fname, Lastname=lname,
                                              Contact=contact,Email=email,Password=password)
                message = "You have Successfully Registred"
                return render(request,"app/login.html",{'msg':message})
            else:
                message="Password and Confirm Password does not match"
                return render(request,"app/register.html",{'msg':message})
