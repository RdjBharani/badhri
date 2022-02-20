from django.shortcuts import render, HttpResponse
from .forms import SignUp


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
        
