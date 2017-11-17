from django.shortcuts import render

# So many comments @ _ @
# Create your views here.

def index(request):
    # pass dynamic data to the template from the view
    # Kind of like flask with their functions
   # name = 'Gold nugget'
    #value = 1000.00
    # Use a context. A dictionary that maps template variable name to Python objects
    # We can access these values using their keys ('...'):
    #context = { 'treasure_name': name,
      #         'treasure_value': value }
    # In order to use these variables in the template, a variable form context must be surrounded in
    # {{}} double braces. Also called mustaches. All {{variables}} are replaced with context dict using the right keys


    # Pass context as third argument in render function
    return render(request, 'index.html', {'treasures': treasures})

# What if you want to pass more than 1 treasure? Create a class. (OOP basics)

class Treasure:
    # define init function and store attributes
    def __init__(self, name, value, material, location):
        self.name = name
        self.value = value
        self.material = material
        self.location = location
    #Then we can create a Treasure object and set it's attributes with one line of code
treasures = [
    Treasure('Gold Nugget', 500.00, 'gold', 'El Dorado, Nevada'),
    Treasure("Fool's Gold", 0, 'Pyrite', 'Idiot creek, Kentucky'),
    Treasure('Coffee can?', 3.00, 'tin', 'Mojave Desert, Arizona')
# Treasure class with be replaced with a database later..
]
