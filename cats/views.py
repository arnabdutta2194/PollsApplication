from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import fields
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from cats.models import Cats, Breed

# Create your views here.

##List Views
class MainView(LoginRequiredMixin, View):
    def get(self, request):
        bc = Breed.objects.all().count()
        cl = Cats.objects.all()

        ctx = {'breed_count': bc, 'cats_list': cl}
        return render(request, 'cats/cats_list.html', ctx)

class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        bl = Breed.objects.all()
        ctx = {'breed_list': bl}
        return render(request, 'cats/breed_list.html', ctx)

#Breed Crud

class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed #Searches for cats/breed_form.html
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed #Searches for cats/breed_confirm_delete.html
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

#Auto Crud

class CatsCreate(LoginRequiredMixin, CreateView):
    model = Cats #Searches for cats/cats_form.html
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatsUpdate(LoginRequiredMixin, UpdateView):
    model = Cats
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatsDelete(LoginRequiredMixin, DeleteView):
    model = Cats  #Searches for cats/cats_confirm_delete.html
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

# We use reverse_lazy rather than reverse in the class attributes
# because views.py is loaded by urls.py and in urls.py as_view() causes
# the constructor for the view class to run before urls.py has been
# completely loaded and urlpatterns has been processed.

# References

# https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-editing/#createview
