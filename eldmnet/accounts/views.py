from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserForm

# Create your views here.
def home(request):
    return render(request, 'accounts/base.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:index'))

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request, 'accounts/registration.html', {'user_form': user_form,
                                                          'registered': registered})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if(user):
            if(user.is_active):
                login(request, user)
                return HttpResponseRedirect(reverse('accounts:dashboard'))
            else:
                return HttpResponse("account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("Username: {} and Password: {}".format(username, password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request, 'accounts/login.html', {})