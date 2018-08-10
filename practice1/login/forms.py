from django import forms
from django.forms import ModelForm
from .models import User
from django.contrib.auth.hashers import  check_password
from .models import User
from django.contrib.auth import authenticate

class loginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    user=None


    # def clean_email(self):
    #   data=self.cleaned_data['email']
    #   if '$' not in data:
    #       raise forms.ValidationError('it should have $')
    #   return data


    def clean(self):
        # import ipdb;
        # ipdb.set_trace()
        # data=self.cleaned_data['password']
        
        # user =User.objects.get(email=self.cleaned_data['email'])
        # if not check_password(self.cleaned_data['password'],user.password):
        #     raise forms.ValidationError('wrong username or password')

        self.user=authenticate(email=self.cleaned_data['email'],password=self.cleaned_data['password'])
        if self.user is None:
            raise forms.ValidationError('wrong username or password')

    

class NewUserForm(ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    user=None
    class Meta:
        model = User
        fields =['email','name','age','gender','password']
    

    def save(self):
        email=self.cleaned_data['email']
        name=self.cleaned_data['name']
        age=self.cleaned_data['age']
        gender=self.cleaned_data['gender']
        password=self.cleaned_data['password']
        a=User(email=email,name=name,age=age,gender=gender)
        a.set_password(password)
        a.save()
        self.user=authenticate(email=self.cleaned_data['email'],password=self.cleaned_data['password'])

    def clean_email(self):
        try:
            user =User.objects.get(email=self.cleaned_data['email'])
            if user!=None:
                raise forms.ValidationError('email already registered')
        except:
            return self.cleaned_data['email']









