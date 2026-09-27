from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse("""<h1>Hey i am a Django Server.</h1>
        <p>hey this is coming from django server.</p>
        <hr>
        <h3 style="color:blue">Hope you like it.</h3>
    
    
    """)



def success(request):
    print("*" * 10)
    return HttpResponse("<h1>Heu this is a success page.</h1>")