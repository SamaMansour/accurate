from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Medicine






def home_view (request, *args, **kwargs):
    return render(request , "home.html", {})
def contact (request):
    if request.method == "POST":
        message_name = request.POST['message-name'];
        message_email = request.POST['message-email'];
        message = request.POST['message'];

        #send an email 
        send_mail (
            message_name,
            message, 
            message_email,
            ['s.jamansour@gmail.com']
        )

        return render(request, "contact.html", {'message_name':message_name})
    else:
        return render(request, "contact.html")


class MedicineCreateView(LoginRequiredMixin, CreateView):
    model = Medicine
    fields = ['name', 'dosage', 'frequency']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



class MedicineListView(ListView):
    model = Medicine
    template_name = 'medcine_view'  # <app>/<model>_<viewtype>.html
    context_object_name = 'Medicines'
 


class MedicineDetailView(DetailView):
    model = Medicine

class MedicineUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Medicine
    fields = ['name', 'dosage', 'frequency']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()



class MedicineDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Medicine
    success_url = '/'

    def test_func(self):
        med = self.get_object()
        if self.request.user == med.name:
            return True
        return False


