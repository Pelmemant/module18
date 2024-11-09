from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


def index(request):
    return render(request, 'func_templates.html')

class Index2(TemplateView):
    template_name = 'class_templates.html'