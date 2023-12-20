from django.contrib import admin
from .models import User,Banner,About,Portfolio
# Register your models here.

class AdminUser(admin.ModelAdmin):
    list_display=("name","email","phone","message")
class AdminBanner(admin.ModelAdmin):
    list_display=("name","image")
class AdminAbout(admin.ModelAdmin):
    list_display=["discription"] 
class AdminPortfolio(admin.ModelAdmin):
    list_display=("id","title","image")   
    
admin.site.register(User,AdminUser)
admin.site.register(Banner,AdminBanner)
admin.site.register(About,AdminAbout)
admin.site.register(Portfolio,AdminPortfolio)
    
