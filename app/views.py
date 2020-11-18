from django.shortcuts import render
from app.models import Proyectos

def home(request):

    proyectos= Proyectos.objects.all()

    return render(request, 'Ahome.html', { "proyectos" : proyectos})