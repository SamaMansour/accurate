from django.shortcuts import render
from django.http import HttpResponse
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