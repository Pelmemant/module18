from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class Knight(TemplateView):
    template_name = 'knights.html'

class Mage(TemplateView):
    template_name = 'mages.html'

class Page(TemplateView):
    template_name = 'page.html'