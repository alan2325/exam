from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

def add(req):
    if req.method=='POST':
        name=req.POST['name']
        email=req.POST['email']
        phone=req.POST['phone']
        alt=req.POST['alt']
        image=req.FILES['image']
        try:
            data=contact.objects.create(name=name,email=email,phone=phone,alt=alt,image=image)
            data.save()
            return redirect(allcontact)
        except:
            messages.warning(req, "Email Already Exits , Try Another Email.")
    return render(req,'add.html')

def single(req,id):
    if 'contact' in req.session:
        data=contact.objects.get(pk=id)
        return render(req,'singlecontact.html',{'data':data})

def allcontact(req):
    data=contact.objects.all()
    return render(req,'allcontact.html',{'data':data})

def delete(req,id):
    data=contact.objects.get(pk=id)
    data.delete()
    return redirect(allcontact)

def edit(req,id):
    data=contact.objects.get(pk=id)
    if req.method=='POST':
        name=req.POST['name']
        email=req.POST['email']
        phone=req.POST['phone']
        alt=req.POST['alt']
        image=req.FILES['image']

        contact.objects.filter(pk=id).update(name=name,email=email,phone=phone,alt=alt,image=image)       

        return redirect(single)
    return render(req,'edit.html',{'data':data})