 
from django.urls import path
from .import views 
urlpatterns = [
    path('', views.home,name='CosmosHome'),
    path('about/', views.about,name='about'),
    path('contact-us/',views.contact,name='contact-us'),
    path('uploaddesign/',views.userupload,name='userupload'),
    path('Products/collection/',views.collection,name='collection'),
    path('Banners/',views.Banners1,name='Banners'),
    path('Products/',views.Products,name='Products'),

    # path('',  views.userupload,name='userupload'),
]