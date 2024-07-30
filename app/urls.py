from django.contrib import admin
from django.urls import path,include
from app import views



urlpatterns = [
   path('', views.index, name='index'),
   path('index/', views.index, name='index'),
   path('login/', views.login_view, name='login'),
   path('register/', views.register, name='register'),
   path('doctor/', views.doctor, name='doctor'),
   path('patient/', views.patient, name='patient'),



   
]