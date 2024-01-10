
from django.urls import path
from .views import home,artical

urlpatterns = [
    path('', home, name="home"),
    path('article/<int:id>', artical, name="article")
    
]