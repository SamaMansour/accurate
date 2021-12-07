from django.shortcuts import render, redirect 
from .forms import UserLoginForm ,UserRegisterForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm , AuthunticationForm
from django.contrib.auth import (authinticate,

get_user_model,
login,
logout


)




#def sign_up_form (request, *args, **kwargs):
#     if request.method == 'POST':
#         form = NewUserForm (request.POST)
#         if form.is_valid():
#             user = form .save()
#             login (request, user)
#             messages.success (request, "User saved successfully")
#             return redirect ("main:homepage")
#             messages.error(request, "unsuccessful registration , Invalid registration")
#             form = NewUserForm(request.POST)
# return render(request =request, template_name = "users/signup.html", context = {"register_form":form })   
    


def login_form (request):
    next =request.get('next')
    form = UserLoginForm (request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authinticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/")

        context = {
            form :form

        }

        return render (request , "users/login.html", context )


    

          
