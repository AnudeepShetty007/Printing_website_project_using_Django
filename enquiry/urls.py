from django.urls import path
from .import views 
urlpatterns = [
    path('', views.enquiry,name='enquiry'),
]