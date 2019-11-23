from django.shortcuts import render
from  visitinglinks.models import One_side

from userupload.models import user_upload
from users.models import Banners
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def orders(request):
    
    myorders = One_side.objects.filter(name=request.user).order_by('id')
    banners=Banners.objects.filter(name=request.user).order_by('id')
    userupload=user_upload.objects.filter(name=request.user).order_by('id')
    return render(request,'myorders/orders.html',{'myorders':myorders,'banners':banners,'userupload':userupload})
    