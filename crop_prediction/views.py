from django.shortcuts import render

# function calling home page in template directory
def home(request):
    return render(request, "home.html")


# function calling when user clicks checkProduction option in homepage
def checkProduction(request):
    return render(request, "user_interface/user_input.html")

# function calling when user clicks predictCrop option in homepage
def predictCrop(request):
    return render(request, "user_interface/predictCrop_userInput.html")
