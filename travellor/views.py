from django.shortcuts import render
from .models import place

# Create your views here.

def index(request):
    place1 = place.objects.all()
    return render(request,"index.html",{"place1":place1})
