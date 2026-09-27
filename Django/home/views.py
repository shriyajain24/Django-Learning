from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, "home/index.html")



def success(request):
    print("*" * 10)
    return HttpResponse("<h1>Heu this is a success page.</h1>")