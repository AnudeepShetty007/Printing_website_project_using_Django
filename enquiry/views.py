from django.shortcuts import render
from  visitinglinks.models import One_side
from django.contrib import messages
from django.core.mail import send_mail
import random
import string
from django.core.files.storage import FileSystemStorage

def random_string_generator(size=6, chars= string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_order_id_generator():
    order_new_id= random_string_generator()
    qs_exists= One_side.objects.filter(order_id= order_new_id).exists()
    if qs_exists:
        return unique_order_id_generator()
    return order_new_id


# Create your views here.
def enquiry(request):
    if request.method == "POST":
        name=request.POST["name"]
        email=request.POST["email"]
        subject=request.POST["subject"]
        message=request.POST["message"]
        image = request.POST["image"]
        quantity=request.POST["quantity"]
        size1=request.POST['size1']
        
        if request.POST.get('1'):
                print("1")
        if request.POST.get('4'):
                print("4")
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
        one_side=One_side(order_id=order_id,name=name,email=email,subject=subject,message=message,image=image,quantity=quantity,size1=size1,size2=size2)
        one_side.save()
        send_mail(
                'Print Cosmos',
                'You have received an order:'+order_id+ ',' +'We will get back you soon',
                'anudeepstty@gmail.com',
                [email],
                fail_silently=False
        )
        messages.success(request,"We have received your order:"+order_id+','+ 'We will get back to you soon')
        return render(request,'users/home.html')