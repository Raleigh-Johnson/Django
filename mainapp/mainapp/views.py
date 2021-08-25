from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    products = ["Cherries","Apples","Oranges","Strawberries","Pears","Watermelon"]
    context = {
        'products': products,
    }
    return render(request, "home.html", context)
