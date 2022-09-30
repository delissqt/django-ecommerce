from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_view(request, *args, **kwargs):
    print(args)
    print('-------')
    print(kwargs)
    print('------->')
    print(request)
    print(request.user)

    return HttpResponse("<h1>Hello World</h1>")# string HTML code


def contact_view(request, *args, **kwargs):
    return HttpResponse("<h1>Contact</h1>")


def about_view(request, *args, **kwargs):
    return HttpResponse("<h1>About page</h1>")

def profile_view(request, *args, **kwargs):
    return HttpResponse("<h1>Profile page</h1>")
