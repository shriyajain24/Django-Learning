import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from vege.models import Recipe

folder = 'public/static/recipe'

if os.path.exists(folder):
    for file in os.listdir(folder):
        name = file.rsplit('.', 1)[0].replace('-', ' ').replace('_', ' ').title()
        Recipe.objects.get_or_create(
            recipe_name=name,
            recipe_description=f"Delicious {name}",
            recipe_image=f"recipe/{file}"
        )
    print("Saari recipes successfully add ho gayi!")
else:
    print("Folder nahi mila!")