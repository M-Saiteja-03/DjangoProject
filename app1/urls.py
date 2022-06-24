from django.contrib import admin
from django.urls import path,include
from app1 import views

admin.site.site_header="Teja's Administration"
admin.site.site_title="Teja's Administration Portal"
admin.site.index_title="Welcome to Teja's Administration Portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),
]
