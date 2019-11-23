 
from django.urls import path
from .import views  as visitingviews
urlpatterns = [
    path('cards/', visitingviews.cards,name='visitingviews'),
    path('cards/one-sided/', visitingviews.one_sided,name='one-sided'),
    
    path('cards/two-sided/', visitingviews.two_sided,name='two-sided'),
]