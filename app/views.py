from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView, DetailView
from .models import *
# Create your views here.

class HomePage(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = "GameHub"
        context['image'] = ProductImage.objects.all()
        return context

class CategoryView(ListView):
    template_name = 'app/filter.html'

    def get_queryset(self):
        return

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        return context