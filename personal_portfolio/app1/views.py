from django.shortcuts import render,redirect
from .models import User,Banner,About,Portfolio,Artical,Comment,WhatIDo
# Create your views here.
def home(request):
    oBnanner = Banner.objects.first()
    oAbout = About.objects.order_by('id').first()
    oProtfolio = Portfolio.objects.all().order_by('id')[0:6]
    aArticle = Artical.objects.all()[0:3]
    oWhatIDo = WhatIDo.objects.all()
    if request.method == 'POST':
        Name = request.POST.get('name','')
        Email = request.POST['email']
        Phone = request.POST.get('phone','')
        Message = request.POST.get('message','')
        oUser = User(name=Name, email=Email, phone=Phone, message= Message)
        oUser.save()
    return render(request,'index.html',{'banner':oBnanner,'about':oAbout,'portfolio':oProtfolio,"artical":aArticle,"WhatIDo":oWhatIDo})

def artical(request,id):
    aArticle = Artical.objects.filter(id=id)
    aComments = Comment.objects.all()
    if request.method == 'POST':
        Name = request.POST.get('name','')
        Email = request.POST['email']
        Message = request.POST.get('message','')
        oComment = Comment(name=Name, email=Email, message= Message)
        oComment.save()
    return render(request,'article.html',{'article':aArticle,"comments":aComments})
    
