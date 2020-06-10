from django.shortcuts import render, redirect
from user.forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# after logging in user will see their customized dashboard
def userDashboard(request):
    return render(request,'user/userDashboard.html')

# for logout
@login_required
def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

# for new user registeration
def userRegister(request):
    context={}
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            messages.success(request, f'Account created')
            user = authenticate(username=username, password=password)
            login(request,user)
            return HttpResponseRedirect(reverse('userDashboard'))
    else:
        form = UserRegisterForm(request.POST)
    context['form']=form
    return render(request,'user/userSignup.html',context)


#for user login
def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('userDashboard'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'user/userLogin.html', {})
