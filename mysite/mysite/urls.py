"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import (
    
    MedicineCreateView,
    MedicineDetailView,
    MedicineListView,
    
)
from pages import views
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)



from pages.views import home_view, MedicineCreateView, MedicineDetailView,MedicineListView,contact
from user.views import register_request , login_request, logout_request, delete_view
from user import views
from django.contrib.auth import views as auth_views


# Routers for pages 
urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', home_view),
    path ('contact/', contact),
    path('create/', MedicineCreateView.as_view(), name='create-medicine'),
    path("register", views.register_request, name="register"),
    path('accounts/profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path("logout", auth_views.LogoutView.as_view(template_name ='users\logout.html'), name="logout"),
    path('meds/', MedicineListView.as_view(template_name ='medicine_view.html'),name ="med_view" ),
    #path('meds/<int:pk>/update/', MedicineUpdateView.as_view(), name='med-update'),
    path('delete/<int:list_id>/', views.delete_view, name='delete')

    #path('medicine/new/', MedicineCreateView.as_view(), name='medicine-form'),
  
   
]