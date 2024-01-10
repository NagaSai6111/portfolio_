from django.contrib import admin
from .models import User,Banner,About,Portfolio,Artical,Comment
# Register your models here.

class AdminUser(admin.ModelAdmin):
    list_display=("name","email","phone","message")
class AdminBanner(admin.ModelAdmin):
    list_display=("name","image")
class AdminAbout(admin.ModelAdmin):
    list_display=["discription"] 
class AdminPortfolio(admin.ModelAdmin):
    list_display=("id","title","image") 
class AdminArtical(admin.ModelAdmin):
    list_display=("img","title","Short_Discription","Large_Discription","createdName","createdAt")  
class AdminComment(admin.ModelAdmin):
    list_display=("name","email","message",'createdAt')
    
admin.site.register(User,AdminUser)
admin.site.register(Banner,AdminBanner)
admin.site.register(About,AdminAbout)
admin.site.register(Portfolio,AdminPortfolio)
admin.site.register(Artical,AdminArtical)    
admin.site.register(Comment,AdminComment)  