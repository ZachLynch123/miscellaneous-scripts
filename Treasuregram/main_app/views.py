from django.shortcuts import render


# Create your views here.

def index(request):
    # pass dynamic data to the template from the view
    # Kind of like flask with their functions
    name = 'Gold nugget'
    value = 1000.00
    # Use a context. A dictionary that maps template variable name to Python objects
    context = { 'treasure_name': name,
               'treasure_value': value }

    # Pass context as third argument in render function
    return render(request, 'index.html', context)