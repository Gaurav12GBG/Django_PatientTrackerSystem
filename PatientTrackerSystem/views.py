## I have created this file ##
from email import message
from django.http import HttpResponse
from django.http.request import validate_host
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")

@login_required
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(message) < 4:
            messages.warning(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email,
                              phone=phone, message=message)
            contact.save()
            messages.success(
                request, "Your message has been successfully sent")

    return render(request, 'contact.html')

@login_required
def addDetails(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        mname = request.POST['mname']
        lname = request.POST['lname']
        email = request.POST['email']
        adharno = request.POST['adharno']
        phone = request.POST['phone']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        occupation = request.POST['occupation']
        maritalstatus = request.POST['maritalstatus']
        religion = request.POST['religion']
        address = request.POST['address']
        state = request.POST['state']
        district = request.POST['district']
        taluka = request.POST['taluka']
        city = request.POST['city']
        pincode = request.POST['pincode']
        diabetes = request.POST['diabetes']
        cancer = request.POST['cancer']
        bloodgroup = request.POST['bloodgroup']
        diseases = request.POST['diseases']
        vaccinestatus = request.POST['vaccinestatus']
        
        lengthOfName = len(fname)+len(mname)+len(lname)
        
        if lengthOfName < 5 or len(email) < 4 or len(phone) < 10 or len(age) < 2 or len(adharno) < 12:
            messages.warning(request, "Please fill the form correctly")
        else:
            patientdetails = PatientInfo(fname=fname, mname=mname, lname=lname, email=email, adharno=adharno, phone=phone, dob=dob, age=age, gender=gender, occupation=occupation, maritalstatus=maritalstatus, religion=religion, address=address, state=state, district=district, taluka=taluka, city=city, pincode=pincode, diabetes=diabetes, cancer=cancer, bloodgroup=bloodgroup, diseases=diseases, vaccinestatus=vaccinestatus)
        
            print(patientdetails)
            
            patientdetails.save()
            messages.success(request, "Thank you! Your all details added successfully!")
        
    return render(request, "addDetails.html")

def registration(request):
    if request.method == 'POST':
        username = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # checks for errorneous
        # username should be under 10 characters
        if len(username) > 10:
            messages.error(
                request, 'Username must be under 10 characters')
            return redirect("registration")

        # user should be alphanumeric
        if not username.isalnum():
            messages.error(
                request, 'Username should only contain letters and numbers')
            return redirect("registration")

        if User.objects.filter(username=username).exists():
            messages.error(
                request, 'Username is already taken, Please try with different !')
            return redirect("registration")

        if User.objects.filter(email=email).exists():
            messages.error(
                request, 'Email is already taken, Please try with different !')
            return redirect("registration")

        # passwortds should match
        if pass1 != pass2:
            messages.error(request, 'Password do not match')
            return redirect("registration")

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        messages.success(
            request, "Youe PTS account has been created successfully! kindly please login..")
        return redirect("login1")

    else:
        return render(request, "registration.html")


def login1(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "successfully logged in !")
            return redirect("home")
        else:
            messages.error(request, "Invalid Credentials, Please try again!")
            return redirect("login1")

    return render(request, "login1.html")


def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out !")
    return redirect("home")


def search(request):
      
    return render(request, "search.html")