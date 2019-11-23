from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from .models import Profile

def register(request):
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        corp= request.POST.get('Issue')
        if form.is_valid():
            user = form.save()
            profile1= Profile(user=user,bio=corp)
            profile1.save()
            username = form.cleaned_data.get('username')
                
            messages.success(request, f' Welcome {username} your acount has been created, Please Login Here')
            return redirect('login')
    else:
        
        form = UserRegisterForm()
    return render(request, 'usersregis/register.html',{'form':form})
    
@login_required
def profile(request):
    return render(request,'usersregis/profile.html')
