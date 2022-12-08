from django.contrib import admin    
from django.urls import path
from .views import index, save, status


urlpatterns = [

    path('', index),   
    path('save', save, name="save"),
    path('status/<int:id>', status, name='status'),
]

