from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView, DetailView
# Create your views here.

class HomePage(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = "GameHub"
        return context