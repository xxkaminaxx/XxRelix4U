from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import PersonalLoginForm

# Create your views here.


def index(request):
    # returns the index.html file
    return render(request, 'index.html')


def logout(request):
    # logs user out
    auth.logout(request)
    messages.success(request, "You have logged out.")
    return redirect(reverse('index'))


def login(request):
    #  returns user to login page
    personal_login_form = PersonalLoginForm()
    return render(request,
                  'login.html', {'personal_login_form': personal_login_form})
