
from django.shortcuts import  render, redirect
from .forms import NewUserForm, RawMedicineForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth import  authenticate 
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib import messages
from .models import Medicine
from django.contrib.auth.decorators import login_required


#signup 
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




#login
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('register')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "users/login.html",
                    context={"form":form})


#logout
def logout_request(request):
    logout(request)
    return redirect('/')


# create a medicine
def medicine_create_view (request):
    my_form:RawMedicineForm(request.GET)
    if request.method == 'POST':
        my_form = RawMedicineForm(request.POST)
        if my_form.is_valid():
            print (my_form.cleaned_data)
            Product.objects.create(title = my_new_title)
        else:
            print(my_form.errors)    
    return render(request = request,
                    template_name = "medicine_create.html"
                   )


@login_required
def profile(request):
    return render(request, 'users/profile.html')


# Medicine Delete
def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")

    return render(request, "delete_view.html", context)
