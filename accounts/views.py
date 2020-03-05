from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import PersonalLoginForm, RegistrationForm

# Create your views here.


def index(request):
    # returns the index.html file
    return render(request, 'index.html')

@login_required  # redirects user to login if they try to access other content
def logout(request):
    # logs user out
    auth.logout(request)
    messages.success(request, "You have logged out.")
    return redirect(reverse('index'))


def login(request):
    # Return a login page
    # when info from form is submited create instance of user
    # (create an account for user)
    # redirects user when logged in and they initially login
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        personal_login_form = PersonalLoginForm(request.POST)
# checks to see if the username and passwords typed in are correct
        if personal_login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

# if user log them in
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have logged in!")
                return redirect(reverse('index'))
                # if incorrect error !
            else:
                personal_login_form.add_error(None,
                                              "Your credentials are incorrect")
    else:
        personal_login_form = PersonalLoginForm()
    return render(request, 'login.html',
                  {'personal_login_form': personal_login_form})


def user_registration(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "congrats! all registered!")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = RegistrationForm()
    return render(request, 'register.html', {
        'registration_form': registration_form})


def personal_profile(request):
    # personal profile page
    # this retrieves user info from db
    user = User.objects.get(email=request.user.email)
    return render(request, 'personal_profile.html', {'personal_profile': user})


def password_email(request):

    return render(request, 'password_reset_email.html')
