from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import SignUp, Userdetails
from .models import *
from django.contrib.auth.decorators import login_required, user_passes_test

def employee(user):
    return user.role == 2

def manager(user):
    return user.role==1

def signup(request):
    form = SignUp
    return render(request,"signup_page.html", {'form':form})

def menupage(request):
    return render(request,"menu.html")

def usersignup(request):
    if request.method=="POST":
        form_data = SignUp(request.POST)
        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.role = 1
            data.save()
            print("\n\ndata:", data)
            return HttpResponse("User created Successfully")
        else:
            return HttpResponse("please enter valid data")
    else:
        form = SignUp
        return render(request,"signup_page.html", {'form':form})
        
def loginpage(request):
    return render(request,"login.html")

def log(request):
    if request.method == "POST":
        xxx= request.POST.get('username')
        yyy = request.POST.get('password')
        user = authenticate(username=xxx, password=yyy)
        if user:
            request.session.set_expiry(6000)
            login(request, user)
            request.session['username'] = xxx
           
            return render(request,'menu.html',{"username":user})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
    
def log_out(request):
    logout(request)
    return redirect('/loginpage')

@login_required()
def creuser(request):
    return render(request,"userdetails.html")

@login_required()
@user_passes_test(manager)
def usercreate(request):
    if request.method =="POST":
        name=request.POST.get("name")
        contact=request.POST.get("contact")
        address=request.POST.get("address")
        dob=request.POST.get("dob")
        user_details=UserDetails(name=name,contact=contact,address=address,dob=dob)
        user_details.save()
        
        return redirect("/viewuser")
    else:
        return render(request,"userdetails.html")
    
@login_required()
@user_passes_test(manager)
def userview(request):
    forms=UserDetails.objects.all()
    return render(request,"viewuser.html",{"data":forms})

@login_required()
@user_passes_test(manager)
def useredit(request, id):  
    data = UserDetails.objects.get(id=id)  
    return render(request,'edituser.html', {'form':data})  

@login_required()
@user_passes_test(manager)
def userupdate(request, id):  
    data=UserDetails.objects.get(id=id)  
    form = Userdetails(request.POST,instance = data)
    if form.is_valid():
        form.save()  
        user=UserDetails.objects.all()
        return render(request,'viewuser.html',{'data':user})
    return render(request, 'edituser.html', {'form': data})

@login_required()
@user_passes_test(manager)
def userdelete(request,id):
    data=UserDetails.objects.get(id=id)
    data.delete()
    user=UserDetails.objects.all()
    return render(request,'viewuser.html',{'data':user})
    