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
   path('create_post/',views.create_post, name='create_post'),
   path('logout/', views.logout_view, name='logout'),
   path('edit/<int:id>/',views.edit, name='edit'),
   path('delete/<int:id>/',views.delete, name='delete'),
   path('create_category/',views.create_category, name='create_category'),



   
]