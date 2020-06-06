from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def checkProduction(request):
    return render(request, "user_interface/user_input.html")

def predictCrop(request):
    return render(request, "user_interface/predictCrop_userInput.html")
