from ast import Not
from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from mysqlx import Auth

from django.contrib.auth import authenticate,logout,login
import mysql.connector as sql 


def Login(request): 
    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']
        
        User = auth.authenticate(username=username, password=password)
    

        if User is not None:
            auth.login(request,User)

            return redirect('admin_page.html')
        else: 
            messages.info(request,'Username or password incorrect ') 
            return redirect('Login')

    else:    
    
        return render( request,  'Login.html')