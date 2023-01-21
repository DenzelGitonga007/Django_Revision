from django.shortcuts import render
# import response
from django.http import HttpResponse

# Create your views here.
# Function based views
# Home page view
def home_view(request):
    # return HttpResponse("<h1>Learn Everyday A World of New Possibilities</h1>")
    # Returning the templates
    return render(request, 'home.html', context = {})

# About view
def about_view(request):
    return render(request, 'about.html')