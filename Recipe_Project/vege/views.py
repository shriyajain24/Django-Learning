from django.shortcuts import render,redirect
from .models import *

# Create your views here.


def recipes(request):
    if request.method == "POST":
        data = request.POST
        
        recipe_image = request.FILES.get("recipe_image")
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
     
       
        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image,
        )
        
        
        return redirect("/")
        
    return render(request, "recipes.html")