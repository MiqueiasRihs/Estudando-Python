from django.shortcuts import render, redirect
from core.models import Evento

# Create your views here.
def lista_eventos(request):
    evento = Evento.objects.all()
    data = {'eventos':evento}
    return render(request, 'agenda.html', data)