# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages 
from django.shortcuts import render
from .forms import loginForm,NewUserForm
from django.http import HttpResponse
from .models import User
from django.contrib.auth.hashers import  check_password
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth

def login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            # try:
            #     user =User.objects.get(email=form.cleaned_data['email'])
            # except:
            #     return HttpResponse('User doesnot exist')
            # if not check_password(form.cleaned_data['password'],user.password):
            #     messages.error(request, "Wrong username or password")
            # else:
            auth.login(request,form.user)
            return HttpResponseRedirect(reverse('home'))
    

    else:
        form = loginForm()

    return render(request, 'login.html', {'form': form})



def signup(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            # import ipdb;
            # ipdb.set_trace()
            user=form.save()
            auth.login(request,form.user)
            return HttpResponseRedirect(reverse('home'))

    else:
        form = NewUserForm()

    return render(request, 'signup.html', {'form': form})


def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html', {'name': request.user.email})
    else:
        return HttpResponseRedirect(reverse('logi'))


def logout(request):
    auth.logout(request)
    
    return HttpResponseRedirect(reverse('logi'))

