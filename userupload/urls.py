from django.urls import path
from .import views 
urlpatterns = [
    path('',  views.userupload,name='userupload'),
    
]