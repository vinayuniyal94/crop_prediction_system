from django.shortcuts import render

def crop_predict(request):
    return render(request, "home.html")

def user_input(request):
    return render(request, "user_interface/user_input.html")
