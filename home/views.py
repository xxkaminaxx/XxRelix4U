from django.shortcuts import render

# Create your views here.


def home_page(request):
    # returns the index.html file
    return render(request, 'index.html')
