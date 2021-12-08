
# #def sign_up_form (request, *args, **kwargs):
# #     if request.method == 'POST':
# #         form = NewUserForm (request.POST)
# #         if form.is_valid():
# #             user = form .save()
# #             login (request, user)
# #             messages.success (request, "User saved successfully")
# #             return redirect ("main:homepage")
# #             messages.error(request, "unsuccessful registration , Invalid registration")
# #             form = NewUserForm(request.POST)
# # return render(request =request, template_name = "users/signup.html", context = {"register_form":form })   
    


# from django.shortcuts import render, redirect

# from django.contrib.auth import (
#     authenticate,
#     get_user_model,
#     login,
#     logout
# )

# from .forms import UserLoginForm, UserRegisterForm


# def login_view(request):
#     next = request.GET.get('next')
#     form = UserLoginForm(request.POST or None)
#     if form.is_valid():
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         user = authenticate(username=username, password=password)
#         login(request, user)
#         if next:
#             return redirect(next)
#         return redirect('/')

#     context = {
#         'form': form,
#     }
#     return render(request, "users/login.html", context)


# def register_view(request):
#     next = request.GET.get('next')
#     form = UserRegisterForm(request.POST or None)
#     if form.is_valid():
#         user = form.save(commit=False)
#         password = form.cleaned_data.get('password')
#         user.set_password(password)
#         user.save()
#         new_user = authenticate(username=user.username, password=password)
#         login(request, new_user)
#         if next:
#             return redirect(next)
#         return redirect('/')

#     context = {
#         'form': form,
#     }
#     return render(request, "users/signup.html", context)


# def logout_view(request):
#     logout(request)
#     return redirect('/')




from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm 

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="users/signup.html", context={"register_form":form})

