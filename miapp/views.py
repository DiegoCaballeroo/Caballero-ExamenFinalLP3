from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

# Create your views here.
def index(request):
    return render(request, 'index.html')

def personas(request):
    return render(request, 'personas.html')


