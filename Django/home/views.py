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
    
    vegetables = ['potato', 'tomato', 'onion', 'cabbage', 'carrot', 'beans', 'peas']

    return render(request, "home/index.html" , context={'peoples' : peoples, 'vegetables' : vegetables})



def success(request):
    print("*" * 10)
    return HttpResponse("<h1>Heu this is a success page.</h1>")