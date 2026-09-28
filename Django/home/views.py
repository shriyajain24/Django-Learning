from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):

    peoples = [
        {'name': 'siya' , 'age' : 20},
        {'name': 'divya' , 'age' : 21},
        {'name': 'esha' , 'age' : 22},
        {'name': 'rita' , 'age' : 17},
        {'name': 'sita' , 'age' : 15},
    ]


    return render(request, "home/index.html" , context={'peoples' : peoples})



def success(request):
    print("*" * 10)
    return HttpResponse("<h1>Heu this is a success page.</h1>")