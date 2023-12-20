from django.shortcuts import render,redirect
from .models import User,Banner,About,Portfolio
# Create your views here.
def home(request):
    oBnanner = Banner.objects.first()
    oAbout = About.objects.order_by('id').first()
    oProtfolio = Portfolio.objects.all().order_by('id')[0:6]
    if request.method == 'POST':
        Name = request.POST.get('name','')
        Email = request.POST['email']
        Phone = request.POST.get('phone','')
        Message = request.POST.get('message','')
        oUser = User(name=Name, email=Email, phone=Phone, message= Message)
        oUser.save()
    return render(request,'index.html',{'banner':oBnanner,'about':oAbout,'portfolio':oProtfolio})


# def contact(request):
#     if request.method == 'POST':
#         Name = request.POST.get('name','')
#         Email = request.POST['email']
#         Phone = request.POST.get('phone','')
#         Message = request.POST.get('message','')
#         oUser = User(name=Name, email=Email, phone=Phone, message= Message)
#         oUser.save()
#         return redirect('')
#     return render(request,'index.html')
