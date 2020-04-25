from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,CreateView

# Create your views here.
def getUser_input(request):
    return render("user_interface/crop_predict_ui.html")
