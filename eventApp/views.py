from django.shortcuts import render
from .models import Event


# Create your views here.


def index(request):
    event = Event.objects.all()[:1]

    context = {"event": event}

    return render(request, 'index.html', context)
