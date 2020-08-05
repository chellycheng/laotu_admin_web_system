from django.shortcuts import render
from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer


# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows events to be viewed or edited
    '''
    queryset = Event.objects.all().order_by('-event_datetime')
    serializer_class = EventSerializer
