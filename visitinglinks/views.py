from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import One_side
@login_required
def cards(request):
    return render(request,'visitinglinks/visitinglinks.html')
@login_required
def one_sided(request):
    return render(request,'visitinglinks/one_sided_cards.html')
@login_required    
def image1(request):
    return render(request,'visitinglinks/image1.html')

@login_required    
def order_mail(request):
    return render(request,'visitinglinks/order_mail.html')

@login_required
def two_sided(request):
    return render(request,'visitinglinks/two_sided_cards.html')

    