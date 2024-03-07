from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render

from .models import Admin, Packages
from .models import Admin, Register
from django.contrib import messages
def homepage(request):
    return render(request,"index.html")
def loginpage(request):
    return render(request,"login.html")
def ttmhome(request):
    return render(request,"ttmhome.html")
def register(request):
    return render(request,"register.html")
def loginfail(request):
   return render(request,"loginfail.html")
def checkadminlogin(request):
    if request.method == "POST":
        adminuname = request.POST["uname"]
        adminpwd = request.POST["pwd"]
        flag = Admin.objects.filter(username=adminuname,password=adminpwd)
        if flag:
            return render(request, "ttmhome.html")
        else:
            return HttpResponse("Login Failed")
def checkregistration(request):
    if request.method == "POST":
        name = request.POST["name"]
        addr = request.POST["addr"]
        email = request.POST["email"]
        phno = request.POST["phno"]
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        cpwd = request.POST["cpwd"]
        if pwd == cpwd:
            if Register.objects.filter(username=uname).exists():
                messages.info(request,"username taken...")
                return render(request,"register.html")
            elif Register.objects.filter(email=email).exists():
                messages.info(request,"email taken...")
                return render(request,"register.html")
            else:
                user = Register.objects.create(name=name, address=addr, email=email, phno=phno, username=uname,password=pwd)
                user.save()
                messages.info(request, "user created...")
                return render(request,"Login.html")
def checkpackages(request):
    if request.method == "POST":
        tcode = request.POST["tourcode"]
        tname = request.POST["tourname"]
        tpack = request.POST["tourpackage"]
        tdesc = request.POST["desc"]
        pack = Packages.objects.create(tourcode=tcode,tourname=tname,tourpackage=tpack,desc=tdesc)
        pack.save()
        messages.info(request,"Data inserted successfully")
        return render(request,"package.html")
    else:
        return render(request, "package.html")