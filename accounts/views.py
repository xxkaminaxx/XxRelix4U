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
    # Return a login page
    # when info from form is submited create instance of user
    # (create an account for user)
    if request.method == "POST":
        personal_login_form = PersonalLoginForm(request.POST)
# checks to see if the username and passwords typed in are correct
        if personal_login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

# if user log them in
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                # if incorrect error !
            else:
                personal_login_form.add_error(None,
                                              "Your credentials are incorrect")
    else:
        personal_login_form = PersonalLoginForm()
    return render(request, 'login.html',
                  {'personal_login_form': personal_login_form})
