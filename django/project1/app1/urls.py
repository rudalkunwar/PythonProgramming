from django.urls import path,include
from .import views

urlpatterns = [path('',views.myfunctioncall,name='index'),path('about',views.about,name='about')]