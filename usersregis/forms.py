from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

# class UserRegisterForm(UserCreationForm):
#     email= forms.EmailField()

#     class Meta:
#         model = User    
#         fields = ['username','email','password1','password2']

class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField(required=True,label="Email")
    username=forms.CharField(min_length=7)

    
    
    

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        # self.fields['username'].widget.attrs.update({'placeholder': 'Enter Valid Username'})
        # self.fields['password1'].widget.attrs.update({'placeholder': 'Enter Password of your choice'})
        self.fields['password1'].help_text = None
        # self.fields['password2'].widget.attrs.update({'placeholder': 'Enter Password again'})
        # self.fields['email'].widget.attrs.update({'placeholder': 'Enter your email-id'})

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        
        
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

        for fieldname in ['username','email' ,'password1', 'password2']:
            self.fields['password1'].help_text = None
           

print (UserRegisterForm())

    
