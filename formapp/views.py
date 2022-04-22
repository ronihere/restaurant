from django.shortcuts import render,redirect
# from django.http import HttpResponse
from django.core.mail import send_mail
from . models import contactform,booktable,subscription
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def contact(request):
    name=request.POST['name']
    email=request.POST['email']
    message=request.POST['message']
    phone=request.POST['phone']


    var1=contactform(name=name,email=email,message=message,phone=phone)
    var1.save()

    messages.error(request,f"Thank you {name} !\nYour response has been recieved." ,extra_tags='contact')
    send_mail(f"MOXE-Restraunt,",
                f"Hey {name}! Thank you for your response. We will contact you if necessary!\n ",
                'from0the0headquarter0of@gmail.com',
                [email],
                fail_silently=True)
    return redirect('/')




def booktable1(request):
    name1 = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    phone = request.POST['phone']
    people = request.POST['people']
    date = request.POST['date']
    time =request.POST['time']


    if User.objects.filter(email=email).first():
        messages.error( request,f"{email}, You are already enrolled ! ",extra_tags='booktable')
        return redirect('/')

    else:
        var2 = booktable(name=name1,email=email,message=message,phone=phone,people=people,date=date,time=time)
        var2.save()
        messages.error(request, f"{email},Your request is recieved but your table hasn't been booked yet .You will listen from us soon", extra_tags='booktable')
        send_mail(f"MOXE-Restraunt,",
                  f"Hey {name1}! Your table hasn't been booked yet .You will listen from us soon for confirmation. Thank you.\nDetails given by you:\n NAME : {name1}\n DATE: {date}\n TIME: {time}\nPlease kindly wait for confirmation from our side!",
                  'from0the0headquarter0of@gmail.com',
                  [email],
                  fail_silently=True)
        return redirect('/')

def subscribe(request):
    email = request.POST['email']
    if User.objects.filter(email=email).first():
        var1=subscription(email=email)
        var1.save()

    return redirect('/')