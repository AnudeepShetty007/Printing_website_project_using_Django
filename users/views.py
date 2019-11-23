from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import contactus
from django.contrib.auth.decorators import login_required
from users.models import Banners
from userupload.models import user_upload



posts = [
    {
        # 'author': 'Anudeep',
         'title': 'Welcome',
        # 'content': 'First post content',
        # 'date_posted': 'August 27, 2018'
    },
    # {
    #     'author': 'Ram',
    #     'title': 'Visiting Card 2',
    #     'content': 'Second post content',
    #     'date_posted': 'August 28, 2018'
    # }
]

def home(request):
    
    return render(request, 'users/home.html')

# Create your views here.
def about(request):
    return render(request, 'users/about.html',{'title': 'Print Cosmos'})

def contact(request):
    if request.method == 'POST':
        
        name= request.POST["name"]
        mobile=request.POST["mobile"]
        
        Email=request.POST["Email"]
        Issue=request.POST["Issue"]
        Query = request.POST["Query"]
        
        
        
        data= contactus(name=name,mobile=mobile,Email=Email,Issue=Issue,Query=Query)
        data.save()
        messages.success(request, f' Thanks for the Valuable time, we will get back to you on this')
        return redirect('CosmosHome')
    else:
        
        return render(request,'users/contact_us.html')


    

from django.core.mail import send_mail
import random
import string
from django.core.files.storage import FileSystemStorage

def random_string_generator(size=6, chars= string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



def unique_order_id_generator():
    order_new_id= random_string_generator()
    qs_exists= user_upload.objects.filter(order_id= order_new_id).exists()
    if qs_exists:
        return unique_order_id_generator()
    return order_new_id


# Create your views here.
def userupload(request):
    if request.method == "POST":
        name=request.POST["name"]
        email=request.POST["email"]
        subject=request.POST["subject"]
        message=request.POST["message"]
        
        quantity=request.POST["quantity"]
        size1=request.POST['size1']
        uploaded_file=request.FILES['myfile']
        
        if size1:
                print("hello")
        else:
                size1=89
        size2=request.POST['size2']
        if size2:
                print("hello")
        else:
                size2=51
        # fs=FileSystemStorage()
        # file_name=fs.save(uploaded_file.name,uploaded_file)
        order_id=unique_order_id_generator()
        upload=user_upload(order_id=order_id,name=name,email=email,subject=subject,message=message,quantity=quantity,size1=size1,size2=size2,myfile=uploaded_file)
        upload.save()
        send_mail(
                'Print Cosmos',
                'You have received an order:'+order_id+ ',' +'We will get back you soon',
                'anudeep.shetty1995@gmail.com',
                [email],
                fail_silently=False
        )
        
        messages.success(request,"We have received your order:"+order_id+','+ 'We will get back to you soon')
        return render(request,'users/home.html')

    else:
        return render(request,'users/userupload.html')


def collection(request):
    return render(request,'users/collection.html')

    
def Banners1(request):
    if request.method == "POST":
        name=request.POST["name"]
        email=request.POST["email"]
        subject=request.POST["subject"]
        message=request.POST["message"]
        image=request.POST["image"]
        quantity=request.POST["quantity"]
        size1=request.POST['size1']
        
        
        if size1:
                print("hello")
        else:
                size1=89
        size2=request.POST['size2']
        if size2:
                print("hello")
        else:
                size2=51
        # fs=FileSystemStorage()
        # file_name=fs.save(uploaded_file.name,uploaded_file)
        order_id=unique_order_id_generator()
        upload=Banners(order_id=order_id,name=name,email=email,subject=subject,message=message,image=image,quantity=quantity,size1=size1,size2=size2)
        upload.save()
        send_mail(
                'Print Cosmos',
                'You have received an order:'+order_id+ ',' +'We will get back you soon',
                'anudeep.shetty1995@gmail.com',
                [email],
                fail_silently=False
        )
        
        messages.success(request,"We have received your order:"+order_id+','+ 'We will get back to you soon')
        return render(request,'users/home.html')

    else:
        return render(request,'users/Banners.html')

@login_required
def Products(request):
    return render(request,'users/Products.html')