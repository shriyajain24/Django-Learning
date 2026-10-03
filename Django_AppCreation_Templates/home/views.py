from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):

    peoples = [
        {'name': 'Siya mehta' , 'age' : 20},
        {'name': 'Divya sharma' , 'age' : 21},
        {'name': 'Esha patel' , 'age' : 22},
        {'name': 'Rita desai' , 'age' : 17},
        {'name': 'Sita jain' , 'age' : 15},
    ]
    
    for people in peoples:
        if people['age'] :
            print("Yes")
        
    
    vegetables = ['potato', 'tomato', 'onion', 'cabbage', 'carrot', 'beans', 'peas']

    return render(request, "home/index.html" , context={'page' : 'Django 2026 Tutorial','peoples' : peoples, 'vegetables' : vegetables})

def about(request):
    context = {'page': 'About'}
    return render(request, "home/about.html", context)

def contact(request):
    context = {'page': 'Contact'}
    return render(request, "home/contact.html", context)

def success(request):
    print("*" * 10)
    return HttpResponse("<h1>Heu this is a success page.</h1>")