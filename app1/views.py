from django.shortcuts import render,HttpResponse
import datetime
from app1.models import Contact
# Create your views here.
def home(request):
    date=datetime.datetime.now()
    msg="Hello!!"
    hours=int(date.strftime("%H"))
    if hours<12:
        msg+="Good Morning"
    elif hours>=12 and hours<16:
        msg+="Good Afternoon"
    elif hours<21:
        msg+="Good Evening"
    else:
        msg+="Gdnt Have a nice sleep"
    return render(request,"home.html",{'msg':msg,'date':date})
def about(request):
    return render(request,'about.html')
def projects(request):
    return render(request,'projects.html')
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        concern=request.POST['concern']
        checks=request.POST['check']
        if checks=="on":
            checks=True
        else:
            checks=False
        ins=Contact(name=name,email=email,phone=phone,concern=concern,checks=checks)
        ins.save()
        print(name,email,phone,concern,checks)
        print("The data has been saved in the db")
        
    return render(request,'contact.html')

