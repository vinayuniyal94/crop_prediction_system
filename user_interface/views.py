from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,CreateView

# Create your views here.
class getUser_input(CreateView):
    template_name = "crop_predict_ui.html"
